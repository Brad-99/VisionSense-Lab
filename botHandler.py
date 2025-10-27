import pydirectinput
import win32gui
from pip._vendor.distlib.compat import raw_input
from datetime import datetime
import requests

import handler
import time
import random
from pynput.keyboard import Key, Controller
from PIL import ImageGrab
import pyttsx3
import os
from socket import *
pydirectinput.FAILSAFE = False
keyboard = Controller()

# Maple window name
MAPLE_WINDOW_NAME = 'MapleStory'

JUMP_KEY = 'alt'

BUFF_TIME = 33 * 1  # Seconds
LOOP_COUNT = 1
skill_3s=time.time()
skill_6s=time.time()
skill_15s=time.time()
skill_60s=time.time()
skill_120s=time.time()
skill_180s=time.time()
summon=time.time()

def startBot():
    # timeout skills
    buffTimeOut = time.time()
    LOOP_COUNT = 1

    time.sleep(3)
    bottom_deck_3()
    while True:
        if handler.botThread.isRunning() and handler.gameMonitorInstance.getPlayerCoords() is not None:
            # Don't touch
            currentTime = time.time()

            ignore_attack = False
            while True:
                if handler.botThread.isRunning() and handler.gameMonitorInstance.getPlayerCoords() is not None:
                    ignore_attack = True
                    bottom_deck_3()
                    # harsh_winter_4()
                    # eastern_outskirts()
                    # gcc2()
                    ignore_attack = False
                    if not ignore_attack:
                        attack()

def attack():
    skills_3s()
    skills_6s()
    skills_15s()
    skills_180s()
    skills_120s()
    skills_60s()
    pydirectinput.press('shift', 1, 0)
    sleep_duration = random.uniform(0.1, 0.4)
    time.sleep(sleep_duration)


def isInRange(targetX, targetY, playerCoords, wantedRange):
    xRange = abs(targetX - playerCoords.x)
    yRange = abs(targetY - playerCoords.y)
    return xRange < wantedRange and yRange < wantedRange


def goTo(targetX, targetY, rangeFromCoords, isRune=False):
    WANTED_RANGE = rangeFromCoords
    if handler.gameMonitorInstance.getPlayerCoords() is not None:

        # Get the updated coordinates from the monitor gui
        currentPlayerLocation = handler.gameMonitorInstance.getPlayerCoords()

        xDistance = targetX - currentPlayerLocation.x
        while abs(xDistance) > WANTED_RANGE and handler.botThread.isRunning():  # Check the X axis
            goToDirection('RIGHT', xDistance) if xDistance > 0 else goToDirection('LEFT', xDistance)
            currentPlayerLocation = handler.gameMonitorInstance.getPlayerCoords()
            xDistance = targetX - currentPlayerLocation.x

        yDistance = targetY - currentPlayerLocation.y
        time.sleep(0.3)
        while abs(yDistance) > WANTED_RANGE and handler.botThread.isRunning():  # Check the Y Axis
            goDown() if yDistance > 0 else goUp(yDistance)
            time.sleep(0.1)
            if isRune:
                time.sleep(0.85)
            currentPlayerLocation = handler.gameMonitorInstance.getPlayerCoords()
            yDistance = targetY - currentPlayerLocation.y


def goToDirection(direction, distance):
    pydirectinput.PAUSE = 0.005
    if abs(distance) >= 25:  # Check if this is long enough for double jump
        pydirectinput.keyDown(direction.lower())
        # pydirectinput.press(JUMP_KEY, 1, 0.05)
        pydirectinput.press(JUMP_KEY, 1, 0)
        pydirectinput.press('c', 1, 0)
        time.sleep(0.01)
        # pydirectinput.press(TP_KEY) - Use me if you are using teleport (Kanna, Mage...)
        pydirectinput.keyUp(direction.lower())
    else:
        # change hold time based on distance
        # the closer the distance, the shorter the hold time
        hold_time = min(0.25, max(0.05, abs(distance) / 100)) 
        holdKey(direction.lower(), hold_time)

# Movements
def holdKey(key, hold_time):
    startTime = time.time()
    while time.time() - startTime < hold_time:
        pydirectinput.keyDown(key)
    pydirectinput.keyUp(key)

def goUp(distance):
    if abs(distance) >= 5:
        pydirectinput.keyDown('up')
        pydirectinput.press(JUMP_KEY) # Adele upjump
        pydirectinput.press(JUMP_KEY) # Adele upjump
        pydirectinput.keyUp('up')
        # pydirectinput.press('x') #rope lift
    else:
        pydirectinput.press("alt")

def goDown():
    pydirectinput.keyDown('down')
    pydirectinput.press(JUMP_KEY)
    sleep_duration = random.uniform(0.9, 1.0)
    time.sleep(sleep_duration)
    #pydirectinput.press('d')
    pydirectinput.keyUp('down')
    #pydirectinput.press('ctrl')

def jumpDown():
    pydirectinput.keyDown('down')
    pydirectinput.press('alt', 1, 0.05)
    sleep_duration = random.uniform(0.29, 0.39)
    time.sleep(sleep_duration)
    pydirectinput.keyUp('down')

# Skills
def skills_3s():
    global skill_3s
    current_time = time.time()
    if current_time - skill_3s >= 3:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('1', 1, 0)
        skill_3s = time.time()
def skills_6s():
    global skill_6s
    current_time = time.time()
    if current_time - skill_6s >= 6:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('a', 1, 0)
        skill_6s = time.time()
def skills_15s():
    global skill_15s
    current_time = time.time()
    if current_time - skill_15s >= 15:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('s', 1, 0)
        skill_15s = time.time()
def skills_60s():
    global skill_60s
    current_time = time.time()
    if current_time - skill_60s >= 60:
        sleep_duration = random.uniform(1.0, 1.5)
        time.sleep(sleep_duration)
        pydirectinput.press('d', 1, 0)
        time.sleep(sleep_duration)
        time.sleep(sleep_duration)
        pydirectinput.press('f', 1, 0)
        skill_60s = time.time()
def skills_120s():
     global skill_120s
     current_time = time.time()
     if current_time - skill_120s >= 120:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('g', 1, 0)
        skill_120s = time.time()
def skills_180s():
     global skill_180s
     current_time = time.time()
     if current_time - skill_180s >= 365:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('b', 1, 0)
        skill_180s = time.time()

def shiesty():
     global summon
     current_time = time.time()
     if current_time - summon >= 60:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        #pydirectinput.press('3', 1, 0)
        time.sleep(0.5)
        jumpDown()
        time.sleep(0.8)
        pydirectinput.press('s')
        time.sleep(1)
        pydirectinput.press('up')
        time.sleep(1)
        pydirectinput.press('3')
        time.sleep(1)
        summon = time.time()
def shiesty2():
     global summon
     current_time = time.time()
     if current_time - summon >= 60:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('3', 1, 0)
        goTo(38,80,14)
        goTo(152,78,6)
        time.sleep(0.4)
        goTo(123,67,6)
        time.sleep(0.5)
        pydirectinput.press('s')
        goTo(123,67,12)
        time.sleep(1)
        pydirectinput.press('3')
        time.sleep(1)
        summon = time.time()

# harsh winter 4
        # goTo(29,72,1) bot left
        # goTo(31,43,1) top left
def harsh_winter_4():
     global summon
     current_time = time.time()
     if current_time - summon >= 60:
        sleep_duration = random.uniform(0.9, 1.05)
        time.sleep(sleep_duration)
        jumpDown()
        goTo(32,72,1)
        pydirectinput.press("2")
        time.sleep(sleep_duration)
        jumpDown()
        time.sleep(sleep_duration)
        pydirectinput.press("3")
        time.sleep(sleep_duration)
        pydirectinput.press("up")
        time.sleep(sleep_duration)
        pydirectinput.press("3")
        time.sleep(sleep_duration)
        jumpDown()
        time.sleep(sleep_duration)
        goTo(132,58,1)
        pydirectinput.press("3")
        goTo(82,58,1)
        summon = time.time()

# eastern_outskirts
        # goTo(33,71,1) bot left
        # goTo(75,71,1) mid bot
        # goTo(110,71,1) bot right
        # goTo(88,41,1) top right
        # goTo(34,38,1) top left
        # goTo(37,54,1) mid left(attack here)


def eastern_outskirts():
    global summon
    current_time = time.time()
    timeout = 30  # seconds
    start_time = time.time()
    if current_time - summon >= 60:
        sleep_duration = random.uniform(0.9, 1.05)
        goTo(36,71,1)
        goTo(75,71,1)
        pydirectinput.press("3")
        goTo(110,71,1)
        pydirectinput.press("3")
        goTo(88,41,1)
        pydirectinput.press("3")
        goTo(34,38,1)
        pydirectinput.press("2")
        # timeout check
        if time.time() - start_time > timeout:
            print("Timeout! Moving to safe point")
        goTo(36,54,1)
        pydirectinput.keyDown('right')
        time.sleep(random.uniform(0.1, 0.2))
        pydirectinput.keyUp('right')
        summon = time.time()

# giant coral colony 2
        # goTo(30,36,1) top left
        # goTo(72,35,1) top mid
        # goTo(138,33,1) top right
        # goTo(112,53,1) mid right
        # goTo(47,67,1) bot left (attack here)
        
def gcc2():
     global summon
     current_time = time.time()
     if current_time - summon >= 60:
        sleep_duration = random.uniform(0.9, 1.05)
        goTo(30,36,1)
        pydirectinput.press("3")
        goTo(72,35,1)
        pydirectinput.press("3")
        goTo(138,33,1)
        pydirectinput.press("3")
        goTo(112,53,1)
        pydirectinput.press("2")
        # time.sleep(sleep_duration)
        goTo(47,67,1)
        pydirectinput.keyDown('right')
        time.sleep(random.uniform(0.1, 0.2))
        pydirectinput.keyUp('right')
        summon = time.time() 

# def enfolding_forest_1()


def bottom_deck_3():
    global summon
    current_time = time.time()
    timeout = 30  # seconds
    start_time = time.time()
    if current_time - summon >= 60:
        sleep_duration = random.uniform(0.9, 1.05)
        goTo(150,78,1)
        goTo(87,78,1)
        pydirectinput.press("3")
        goTo(40,78,1)
        pydirectinput.press("3")
        goTo(50,49,1)
        pydirectinput.press("3")
        goTo(90,49,1)
        pydirectinput.press("2")
        goTo(150,64,1)
        # timeout check
        if time.time() - start_time > timeout:
            print("Timeout! Moving to safe point")
            goTo(150,64,1)
        pydirectinput.keyDown('left')
        time.sleep(random.uniform(0.1, 0.2))
        pydirectinput.keyUp('left')
        summon = time.time()