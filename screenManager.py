import time
import mss
import numpy as np
from PIL import ImageGrab  # kept for other callers; minimap capture uses mss


class Screen:
    def __init__(self, hpBarPos=None, miniMapPos=None):
        self.hpBarPos = hpBarPos
        self.miniMapPos = miniMapPos

    def setHpBarPos(self, pos):
        self.hpBarPos = pos

    def getHpBarPos(self):
        return self.hpBarPos

    def setMiniMapPos(self, pos):
        self.miniMapPos = pos

    def getMiniMapPos(self):
        return self.miniMapPos


screen = Screen()

_mss_instance = mss.mss()  # reuse to avoid leaking GDI handles

def getMiniMapScreenshot():
    if screen.miniMapPos is None:
        print('ERROR: MiniMap object is None')
    else:
        miniMapPos = screen.miniMapPos
        left = miniMapPos[0].x
        top = miniMapPos[0].y
        width = max(1, miniMapPos[1].x - miniMapPos[0].x)
        height = max(1, miniMapPos[1].y - miniMapPos[0].y)
        try:
            shot = _mss_instance.grab({"left": left, "top": top, "width": width, "height": height})
            # mss returns BGRA; convert to RGB to match previous behavior
            arr = np.array(shot)
            if arr.shape[-1] == 4:
                arr = arr[:, :, :3][:, :, ::-1]  # drop alpha, swap BGR->RGB
            return arr
        except Exception as e:
            print(f'ERROR: MiniMap screenshot failed: {e}')
            time.sleep(0.5)
            return None
