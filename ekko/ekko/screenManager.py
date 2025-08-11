from PIL import ImageGrab


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

def getMiniMapScreenshot():
    if screen.miniMapPos is None:
        print('ERROR: MiniMap object is None')
    else:
        miniMapPos = screen.miniMapPos
        screenshotOfPos = ImageGrab.grab(bbox=(miniMapPos[0].x, miniMapPos[0].y, miniMapPos[1].x, miniMapPos[1].y))

        return screenshotOfPos
