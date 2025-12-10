import time
import mss
from PIL import Image, ImageGrab


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
_mss_instance = mss.mss()  # reuse to避免 GDI handle 泄漏


def getMiniMapScreenshot():
    if screen.miniMapPos is None:
        print('ERROR: MiniMap object is None')
        return None

    miniMapPos = screen.miniMapPos
    left = miniMapPos[0].x
    top = miniMapPos[0].y
    width = max(1, miniMapPos[1].x - miniMapPos[0].x)
    height = max(1, miniMapPos[1].y - miniMapPos[0].y)

    try:
        shot = _mss_instance.grab({"left": left, "top": top, "width": width, "height": height})
        # 保持與 ImageGrab 相同的 PIL Image (RGB) 輸出
        return Image.frombytes("RGB", shot.size, shot.rgb)
    except Exception as e:
        print(f'ERROR: MiniMap screenshot failed: {e}')
        time.sleep(0.5)
        # 失敗時退回 ImageGrab，確保取到圖
        try:
            return ImageGrab.grab(bbox=(left, top, left + width, top + height))
        except Exception:
            return None
