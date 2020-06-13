import multitimer
import time
import datetime
import sys


class RepeatingTimer(object):
    def __init__(self, function, interval: int):
        self.function = function
        self.interval = interval
        self.timer = multitimer.RepeatingTimer(interval=self.interval, function=self.function, count=sys.maxsize, runonstart=False)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()
