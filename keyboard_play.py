#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.6),
    on November 23, 2020, at 17:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""


from __future__ import absolute_import, division

import pandas as pd
import sdl2
from PIL import Image
from pyboy import PyBoy
import ctypes
from time import sleep
import os
from command_handler import command_handler
from pyboy_controller import pyboy_controller
import time
from simulated_eeg import simulated_eeg
from cca_handler import cca_handler



num_seconds = 3 # changing this will affect the time taken for each command
num_targets = 8
start_time = time.time()
elapsed = 0
# currently works only if speedrun is on! Bad!
speedrun = True # disregard control of number of seconds per command
save_state = True
load_state = True
commands_per_sec = 30

# simulated data control
eeg = simulated_eeg(num_targets=num_targets, num_seconds=num_seconds) # must match with cca handler
target = 0
eeg_data = eeg.get_signals(target=target) # numpy array for all channels - set initial target 
actions = []

#Initialize PyBoy
# load rom through PyBoy
# if there is a state file, load it
dir_path = os.path.dirname(os.path.realpath(__file__))
rom_dir = os.path.join(dir_path, 'roms')
pyboy = PyBoy(os.path.join(rom_dir, 'Pokemon.gb'))
if os.path.exists(os.path.join(rom_dir, 'simulated_game.state')) and load_state:
    l_state = open("roms/simulated_game.state", "rb")
    pyboy.load_state(l_state)


# set up PyBoy screen support
bot_sup = pyboy.botsupport_manager()
scrn = bot_sup.screen()

# init image
screen_colors = scrn.screen_ndarray()
img = Image.fromarray(screen_colors)
img.save('game.jpg')

# minimize PyBoy window
pyboy_handle = ctypes.windll.user32.FindWindowW(None, "PyBoy")
ctypes.windll.user32.ShowWindow(pyboy_handle, 6)

# init controller
controller = pyboy_controller(pyboy)

# init command handler
# handler = command_handler(controller)
handler = cca_handler(controller=controller, num_targets=num_targets, num_seconds=num_seconds)

print("prepare steps done")


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
# psychopyVersion = '2020.2.6'
# expName = 'online'  # from the Builder filename that created this script
# expInfo = {'participant': '', 'session': '001'}
# dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
# if dlg.OK == False:
#     core.quit()  # user pressed cancel
# expInfo['date'] = data.getDateStr()  # add a simple timestamp
# expInfo['expName'] = expName
# expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
# filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
# thisExp = data.ExperimentHandler(name=expName, version='',
#                                  extraInfo=expInfo, runtimeInfo=None,
#                                  originPath='C:\\Users\\sulta\\OneDrive\\Desktop\\Capstone Project PsychoPy\\online\\online.py',
#                                  savePickle=True, saveWideText=True,
#                                  dataFileName=filename)
# save a log file for detail verbose info
# logFile = logging.LogFile(filename + '.log', level=logging.EXP)
# logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000, -1.000, -1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
# expInfo['frameRate'] = win.getActualFrameRate()
# expInfo['frameRate'] = 120
# if expInfo['frameRate'] != None:
#     frameDur = 1.0 / round(expInfo['frameRate'])
# else:
#     frameDur = 1.0 / 60.0  # could not measure, so guess

frameDur = 1.0 / 60.0 # just guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()

# Initialize components for Routine "setup"
setupClock = core.Clock()

# Initialize components for Routine "game"
gameClock = core.Clock()
# Import signal for Stimuli
from scipy import signal as sg

image = visual.ImageStim(
    win=win,
    name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75, 0.75),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "predict"
predictClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
welcomeComponents = []
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "game"-------
continueRoutine = True
# update component parameters for each repeat
image.setImage('game.jpg')
# keep track of which components have finished
gameComponents = [image]
for thisComponent in gameComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
gameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "game"-------
while continueRoutine:
    # get current time
    t = gameClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=gameClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # tick pyboy, save new image of screen
    pyboy.tick()
    screen_colors = scrn.screen_ndarray()
    img = Image.fromarray(screen_colors)
    img.save('game.jpg')

    # update component parameters for each frame
    image.setImage('game.jpg')

   

    ##################### EACH FRAME POG ###############################

    # sending space key or zero will mean non-action
    # otherwise, send targets 1-8 using the number keys
    key = defaultKeyboard.getKeys(keyList=["0", "1", "2", "3", "4", "5", "6", "7", "8", "up", "down", "left", "right", "space", "escape"])
    if "escape" in key or endExpNow:
        # save the game state if save_state flag is on
        print('-'*10, "\tActions:\t", "-"*10)
        print([i for i in actions])
        print('-'*20)
        if save_state:
            s_state = open("roms/simulated_game.state", "wb")
            pyboy.save_state(s_state)
            print('game state saved')
        core.quit()
    elif "0" in key or "num_0" in key or "space" in key:
        # non action
        target = 0 
    elif "1" in key or "num_1" in key:
        # x
        target = 1
    elif "2" in key or "num_2" in key:
        # z
        target = 2
    elif "3"  in key or "num_3" in key or "up" in key:
        # up
        target = 3
    elif "4" in key or "num_4" in key or "left" in key:
        # left
        target = 4
    elif "5" in key or "num_5" in key or "right" in key:
        # right
        target = 5
    elif "6" in key or "num_6" in key or "down" in key:
        # down
        target = 6
    elif "7" in key or "num_7" in key:
        # start
        target = 7
    elif "8" in key or "num_8" in key:
        # select
        target = 8


    # print('\nKeyboard selected target {}\n'.format(target))

    if (frameN % int(60 / commands_per_sec) == 0 and frameN != 0) or speedrun:
        elapsed = time.time() - start_time
        # if not speedrun:
        #     print('time elapsed = {} s'.format(elapsed))
        print('frame\t', frameN)
        eeg_data = eeg.get_signals(target=target)
        action = handler.predict(eeg_data)
        actions.append(action)
        start_time = time.time()

    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in gameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "game"-------
for thisComponent in gameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# the Routine "game" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "predict"-------
continueRoutine = True
# update component parameters for each repeat
# PREDICT BABY
# keep track of which components have finished
predictComponents = []
for thisComponent in predictComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
predictClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "predict"-------
while continueRoutine:
    # get current time
    t = predictClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=predictClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in predictComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "predict"-------
for thisComponent in predictComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "predict" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
# thisExp.saveAsWideText(filename + '.csv', delim='auto')
# thisExp.saveAsPickle(filename)
# logging.flush()
# make sure everything is closed down

thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
