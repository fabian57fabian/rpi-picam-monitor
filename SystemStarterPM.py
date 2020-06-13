import time
import datetime
import os
import json
import logging
from PiCamConnector import PiCamConnector
from RepeatingTimer import RepeatingTimer


class PlantMonitor:
    def __init__(self, cam_connector):
        logging.info("Creating PlantMonitor")
        self.cam_connector = cam_connector
        self.images_folder = ''

    def take_oneshot(self):
        logging.debug("Taking one shot.")
        filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
        path = os.path.join(self.images_folder, filename)
        logging.debug("Saving image to %s" % path)
        self.cam_connector.saveCamImage(path)


def read_Settings(settings_path):
    print("Reading settings file")
    with open(settings_path, 'r') as json_file:
        settings = json.load(json_file)
    return settings


if __name__ == '__main__':
    settings = read_Settings('settings.json')
    debug, interval, images_folder, res = settings['debug'], settings['interval'], settings['images_folder'], settings[
        'resolution']
    print("Settings file readed: {}".format(settings))
    logging_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'all_logs.log')
    logging.basicConfig(filename=logging_file, level=logging.DEBUG if debug else logging.INFO,
                        format="%(asctime)s:%(levelname)s:%(message)s")
    print("Logging will be visible in file %s" % logging_file)
    cam_connector = PiCamConnector()
    cam_connector.setResolution(res[0], res[1])
    monitorer = PlantMonitor(cam_connector)
    monitorer.images_folder = images_folder
    timer = RepeatingTimer(monitorer.take_oneshot, interval)
    logging.info("Starting continous timer with interval %d" % interval)
    timer.start()
    print("System Started. Working...")
    # And now doing the first iterazione (instead of waiting for [interval]
    monitorer.take_oneshot()
    while True:
        time.sleep(10)
