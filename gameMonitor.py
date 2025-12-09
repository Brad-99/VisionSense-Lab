from PIL import Image
import screenManager
import gui
import handler
import utils
import numpy
import datetime
import requests
import time

playerIcon = Image.open(r'C:\Users\rayra\Code\maple\pics\playerIcon.png')

class GameMonitor:
    def __init__(self, currentHp=None, currentPlayerCoords=None):
        self.currentPlayerCoords = currentPlayerCoords
        self.runeCoords = None

    def setPlayerCoords(self, currentPlayerCoords):
        self.currentPlayerCoords = currentPlayerCoords

    def getPlayerCoords(self):
        return self.currentPlayerCoords


    def start(self):

        while True:
            if handler.gameMonitorThread.isRunning():  # While the running flag is True
                # Player Coords
                currentPlayerLocation = findCoordsOfColor()
                if currentPlayerLocation is not None:
                    self.setPlayerCoords(currentPlayerLocation)
                    gui.updateCurrentCoordinate(currentPlayerLocation)  # Update the live coords in gui
                time.sleep(0.05)
            else:
                time.sleep(0.2)

def findCoordsOnMiniMap(innerIcon):
    miniMapImage = screenManager.getMiniMapScreenshot()
    innerIconArr = numpy.asarray(innerIcon)
    miniMapArr = numpy.asarray(miniMapImage)

    innerIconArr_y, innerIconArr_x = innerIconArr.shape[:2]
    miniMapArr_y, miniMapArr_x = miniMapArr.shape[:2]

    stopX = miniMapArr_x - innerIconArr_x + 1
    stopY = miniMapArr_y - innerIconArr_y + 1

    for x in range(0, stopX):
        for y in range(0, stopY):
            x2 = x + innerIconArr_x
            y2 = y + innerIconArr_y
            pic = miniMapArr[y:y2, x:x2]
            test = (pic == innerIconArr)
            if test.all():
                return utils.Point(x, y)
    return None

def findCoordsOfColor(target_color=(255, 239, 0), tolerance=10):
    miniMapImage = screenManager.getMiniMapScreenshot()
    miniMapArr = numpy.asarray(miniMapImage)

    # Ensure target color is a NumPy array
    target_color = numpy.array(target_color)

    # Calculate the absolute difference for each channel
    diff = numpy.abs(miniMapArr - target_color)

    # Find pixels where all differences are within the tolerance
    match = numpy.all(diff <= tolerance, axis=-1)

    # Get the indices of the first match
    coords = numpy.argwhere(match)

    if coords.size > 0:
        y, x = coords[0]  # First matching pixel
        return utils.Point(x, y)

    return None
