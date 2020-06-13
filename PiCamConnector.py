import os
import io
import time
from picamera import PiCamera
import logging


class PiCamConnector():
    def __init__(self):
        logging.info("Creating Pi Cam Connector")
        self.camera = PiCamera()

    def setRotation(self, rotation: int):
        self.camera.rotation = rotation

    def setResolution(self, x: int, y: int):
        logging.debug("Resolution changed to (%d, %d)" % (x, y))
        self.camera.resolution = (x, y)

    def saveCamImage(self, filename: str):
        self.camera.start_preview()
        self.camera.capture(filename)
        self.camera.stop_preview()

    def getCamImage(self):
        # Create the in-memory stream
        stream = io.BytesIO()
        self.camera.start_preview()
        time.sleep(2)
        self.camera.capture(stream, format='jpeg')
        # "Rewind" the stream to the beginning so we can read its content
        stream.seek(0)
        # P.S. better to convert it into PIL image with PIL.Image.open(stream)
        return stream
