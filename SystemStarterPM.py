import time
import datetime
import os
import json
from PiCamConnector import PiCamConnector
from RepeatingTimer import RepeatingTimer


class PlantMonitor:
    def __init__(self, cam_connector, debug=False):
        self.debug = debug
        self.cam_connector = cam_connector
        self.images_folder = ''

    def take_oneshot(self):
        print("One Shot!")
        image = self.cam_connector.getImage()
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
        image.save(os.path.join(self.images_folder, filename))


def read_Settings(settings_path):
    with open(settings_path, 'r') as json_file:
        settings = json.load(json_file)
    return settings


if __name__ == '__main__':
    settings = read_Settings('settings.json')
    debug, interval, images_folder, res = settings['debug'], settings['interval'], settings['images_folder'], settings[
        'resolution']
    cam_connector = PiCamConnector(debug)
    cam_connector.setResolution(res[0], res[1])
    monitorer = PlantMonitor(cam_connector, debug)
    monitorer.images_folder = images_folder
    timer = RepeatingTimer(monitorer.take_oneshot, interval)
    timer.start()
    while True:
        time.sleep(10)
