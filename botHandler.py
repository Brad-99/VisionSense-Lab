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
fma_bite=time.time()
fma_omen=time.time()
fma_darkomen=time.time()
fma_shurrikane=time.time()
fma_seren=time.time()
summon=time.time()

def startBot():
    # timeout skills
    buffTimeOut = time.time()
    LOOP_COUNT = 1

    while True:
        if handler.botThread.isRunning() and handler.gameMonitorInstance.getPlayerCoords() is not None:
            # Don't touch
            currentTime = time.time()
            # Buffs and sync methods
            #if currentTime > buffTimeOut:  # Every 3 minutes
            #    doBuff()
            #    buffTimeOut = time.time() + BUFF_TIME
            # fma_nw()
            # time.sleep(1)
            # fma_nw2()
            # continued
            # goTo(40s 57, 10)
            # goTo(162, 57, 10)
            # if (LOOP_COUNT % 5) == 0:
            #     pydirectinput.keyDown('x')
            #     time.sleep(0.5)
            # LOOP_COUNT += 1

            # goTo(172,70,18)
            # shiesty() 
            # goTo(30,70,18)

            while True:
                if handler.botThread.isRunning() and handler.gameMonitorInstance.getPlayerCoords() is not None:
                    attack()
                    # shiesty3()
                    western_outskirts()
            

 
            #### Burning Royal Lib 1 ###
            #goTo(56, 42, 14)
            #goTo(166, 42, 14)c
            #if (LOOP_COUNT % 10) == 0:
            #    pydirectinput.keyDown('up')
            #    pydirectinput.press('v') #assaulter
            #    pydirectinput.keyUp("up")
            #    time.sleep(0.5)
            #    pydirectinput.press('q') #dark flare
            #    time.sleep(0.2)
            #    goTo(60, 15, 14)
            #    pydirectinput.press('1') #erda fountain
            #LOOP_COUNT += 1

#def doBuff():
#    print('Doing buffs')
#    # Define your buffs
#    pydirectinput.press('0')
#    time.sleep(0.2)
#    pydirectinput.press('8')

def attack():
    fma_nw()
    fma_nw2()
    #fma_nw3()
    fma_nw4()
    fma_nw5()
    pydirectinput.press('shift', 1, 0)
    #pydirectinput.press('a')
    time.sleep(0.6)


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
        time.sleep(0.02)
        pydirectinput.press('c', 1, 0)
        time.sleep(0.01)
        attack()
        # pydirectinput.press(TP_KEY) - Use me if you are using teleport (Kanna, Mage...)
        pydirectinput.keyUp(direction.lower())
    else:
        holdKey(direction.lower(), 0.25)


def holdKey(key, hold_time):
    startTime = time.time()
    while time.time() - startTime < hold_time:
        pydirectinput.keyDown(key)
    pydirectinput.keyUp(key)

def goUp(distance):
    if abs(distance) >= 5:
        pydirectinput.press('x') #rope lift
    else:
        pydirectinput.press("alt")
    time.sleep(1.2)

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
def fma_nw():
    global fma_bite
    current_time = time.time()
    if current_time - fma_bite >= 13:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('n', 1, 0)
        fma_bite = time.time()
def fma_nw2():
    global fma_omen
    current_time = time.time()
    if current_time - fma_omen >= 5:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('d', 1, 0)
        fma_omen = time.time()
def fma_nw3():
    global fma_darkomen
    current_time = time.time()
    if current_time - fma_darkomen >= 90:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('s', 1, 0)
        fma_darkomen = time.time()
def fma_nw4():
     global fma_shurrikane
     current_time = time.time()
     if current_time - fma_shurrikane >= 200:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('a', 1, 0)
        fma_shurrikane = time.time()
def fma_nw5():
     global fma_seren
     current_time = time.time()
     if current_time - fma_seren >= 250:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('b', 1, 0)
        fma_seren = time.time()

def shiesty():
     global summon
     current_time = time.time()
     if current_time - summon >= 60:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        #pydirectinput.press('9', 1, 0)
        time.sleep(0.5)
        jumpDown()
        time.sleep(0.8)
        pydirectinput.press('s')
        time.sleep(1)
        pydirectinput.press('up')
        time.sleep(1)
        pydirectinput.press('9')
        time.sleep(1)
        summon = time.time()
def shiesty2():
     global summon
     current_time = time.time()
     if current_time - summon >= 60:
        sleep_duration = random.uniform(0.29, 0.39)
        time.sleep(sleep_duration)
        pydirectinput.press('9', 1, 0)
        goTo(38,80,14)
        goTo(152,78,6)
        time.sleep(0.4)
        goTo(123,67,6)
        time.sleep(0.5)
        pydirectinput.press('s')
        goTo(123,67,12)
        time.sleep(1)
        pydirectinput.press('9')
        time.sleep(1)
        summon = time.time()
9
# harsh winter 4
        # goTo(29,72,1) bot left
        # goTo(31,43,1) top left
def shiesty3():
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
        pydirectinput.press("9")
        time.sleep(sleep_duration)
        pydirectinput.press("up")
        time.sleep(sleep_duration)
        pydirectinput.press("9")
        time.sleep(sleep_duration)
        jumpDown()
        time.sleep(sleep_duration)
        goTo(132,58,1)
        pydirectinput.press("9")
        goTo(82,58,1)
        summon = time.time()

# western_outskirts
        # goTo(33,71,1) bot left
        # goTo(71,71,1) mid bot
        # goTo(106,71,1) bot right
        # goTo(154,71,1) off the cliff
        # goTo(89,41,1) top right
        # goTo(54,41,1) top left(attack here)

def western_outskirts():
     global summon
     current_time = time.time()
     if current_time - summon >= 60:
        sleep_duration = random.uniform(0.9, 1.05)
        time.sleep(sleep_duration)
        goTo(33,71,1)
        pydirectinput.press("9")
        time.sleep(sleep_duration)
        goTo(71,71,1)
        pydirectinput.press("9")
        time.sleep(sleep_duration)
        goTo(106,71,1)
        pydirectinput.press("9")
        time.sleep(sleep_duration)
        goTo(89,41,1)
        pydirectinput.press("2")
        time.sleep(sleep_duration)
        goTo(54,41,1)
        summon = time.time()