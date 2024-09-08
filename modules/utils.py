import cv2
import os
import time

class Timer(object):
    """定时器类"""
    end_time: float

    def __init__(self, interval: float):
        self.end_time = time.perf_counter() + interval

    def timeout(self) -> bool:
        return time.perf_counter() >= self.end_time

def readimage(name):
    filepath = os.path.join(os.path.dirname(__file__), "../resources/" + name + ".png")
    return cv2.imread(filepath, cv2.IMREAD_UNCHANGED)

def writeimage(name, image):
    filepath = os.path.join(os.path.dirname(__file__), "../saved/" + name + ".png")
    try:
        cv2.imwrite(filepath, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 3])
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    
_onclicked = None

def _callback(x, y):
    print(f"点击 X: {x} Y: {y}")
    if _onclicked is not None:
        _onclicked(x, y, False)

def createpreview(onclicked):
    global _onclicked
    _onclicked = onclicked

def showpreview(image, wait=1):
    pass

def destroypreview():
    pass