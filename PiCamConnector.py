import os
import time
from picamera import PiCamera
import logging


class PiCamConnector():
    def __init__(self):
        logging.info("Creating Pi Cam Connector")
        self.camera = PiCamera()

    def setResolution(self, x: int, y: int):
        logging.debug("Resolution changed to (%d, %d)" % (x, y))
        self.camera.resolution = (x, y)

    def saveCamImage(self, filename: str):
        self.camera.start_preview()
        self.camera.capture(filename)
        self.camera.stop_preview()

    def getCamImage(self):
        # TODO get image
        self.camera.start_preview()
        time.sleep(.2)
        self.camera.stop_preview()
