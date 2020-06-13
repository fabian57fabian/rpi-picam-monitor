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
        image = self.cam_connector.getImage()
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
        path = os.path.join(self.images_folder, filename)
        logging.debug("Saving image to %s" % path)
        image.save(path)


def read_Settings(settings_path):
    print("Reading settings file")
    with open(settings_path, 'r') as json_file:
        settings = json.load(json_file)
    return settings


if __name__ == '__main__':
    settings = read_Settings('settings.json')
    debug, interval, images_folder, res = settings['debug'], settings['interval'], settings['images_folder'], settings[
        'resolution']
    logging.info("Settings file readed: {}".format(settings))
    logging.basicConfig(filename='all_logs.log', level=logging.DEBUG if debug else logging.INFO)
    cam_connector = PiCamConnector()
    cam_connector.setResolution(res[0], res[1])
    monitorer = PlantMonitor(cam_connector)
    monitorer.images_folder = images_folder
    timer = RepeatingTimer(monitorer.take_oneshot, interval)
    logging.info("Starting continous timer with interval %d" % interval)
    timer.start()
    while True:
        time.sleep(10)
