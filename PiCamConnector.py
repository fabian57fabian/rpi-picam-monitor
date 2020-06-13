import os
from picamera import PiCamera


class PiCamConnector():
    def __init__(self, debug=False):
        self.debug = debug
        self.camera = PiCamera()

    def setResolution(self, x: int, y: int):
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
