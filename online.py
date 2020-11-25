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

from cortex import Cortex
import pandas as pd
import sdl2
from PIL import Image
from pyboy import PyBoy
import ctypes
from time import sleep
import os
from command_handler import command_handler
from pyboy_controller import pyboy_controller

# Initialize our variables
cortex = Cortex(None)
cortex.do_prepare_steps()
# generator = cortex.sub_request(['eeg'])
generator = cortex.sub_request_pow(['pow'])
next(generator).queue
# data_columns = ["P7", "O1", "O2", "P8", "TIME"]
data_columns = ["O1/theta","O1/alpha","O1/betaL","O1/betaH","O1/gamma",
                "O2/theta","O2/alpha","O2/betaL","O2/betaH","O2/gamma", "TIME"]

#Initialize PyBoy
# load rom through PyBoy
dir_path = os.path.dirname(os.path.realpath(__file__))
rom_dir = os.path.join(dir_path, 'roms')
pyboy = PyBoy(os.path.join(rom_dir, 'Pokemon.gb'))


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
handler = command_handler(controller)

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
psychopyVersion = '2020.2.6'
expName = 'online'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='C:\\Users\\sulta\\OneDrive\\Desktop\\Capstone Project PsychoPy\\online\\online.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

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
expInfo['frameRate'] = win.getActualFrameRate()
expInfo['frameRate'] = 120
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

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

square1 = visual.Rect(
    win=win, name='square1', units='pix',
    width=(200, 200)[0], height=(200, 200)[1],
    ori=0, pos=(0, 400),
    lineWidth=1, lineColor=[1, 1, 1], lineColorSpace='rgb',
    fillColor=[1, 1, 1], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
square2 = visual.Rect(
    win=win, name='square2', units='pix',
    width=(200, 200)[0], height=(200, 200)[1],
    ori=0, pos=(-400, 0),
    lineWidth=1, lineColor=[1, 1, 1], lineColorSpace='rgb',
    fillColor=[1, 1, 1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
square3 = visual.Rect(
    win=win, name='square3', units='pix',
    width=(200, 200)[0], height=(200, 200)[1],
    ori=0, pos=(400, 0),
    lineWidth=1, lineColor=[1, 1, 1], lineColorSpace='rgb',
    fillColor=[1, 1, 1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
square4 = visual.Rect(
    win=win, name='square4', units='pix',
    width=(200, 200)[0], height=(200, 200)[1],
    ori=0, pos=(0, -400),
    lineWidth=1, lineColor=[1, 1, 1], lineColorSpace='rgb',
    fillColor=[1, 1, 1], fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
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

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

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
gameComponents = [square1, square2, square3, square4, image]
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

    # *square1* updates
    if square1.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        square1.frameNStart = frameN  # exact frame index
        square1.tStart = t  # local t and not account for scr refresh
        square1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square1, 'tStartRefresh')  # time at next scr refresh
        square1.setAutoDraw(True)
    # if square1.status == STARTED:
    #     # is it time to stop? (based on global clock, using actual start)
    #     if tThisFlipGlobal > square1.tStartRefresh + 3 - frameTolerance:
    #         # keep track of stop time/frame for later
    #         square1.tStop = t  # not accounting for scr refresh
    #         square1.frameNStop = frameN  # exact frame index
    #         win.timeOnFlip(square1, 'tStopRefresh')  # time at next scr refresh
    #         square1.setAutoDraw(False)
    if square1.status == STARTED:  # only update if drawing
        square1.setOpacity(sg.square(2 * np.pi * 15 * t), log=False)

    # *square2* updates
    if square2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        square2.frameNStart = frameN  # exact frame index
        square2.tStart = t  # local t and not account for scr refresh
        square2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square2, 'tStartRefresh')  # time at next scr refresh
        square2.setAutoDraw(True)
    # if square2.status == STARTED:
    #     # is it time to stop? (based on global clock, using actual start)
    #     if tThisFlipGlobal > square2.tStartRefresh + 3 - frameTolerance:
    #         # keep track of stop time/frame for later
    #         square2.tStop = t  # not accounting for scr refresh
    #         square2.frameNStop = frameN  # exact frame index
    #         win.timeOnFlip(square2, 'tStopRefresh')  # time at next scr refresh
    #         square2.setAutoDraw(False)
    if square2.status == STARTED:  # only update if drawing
        square2.setOpacity(sg.square(2 * np.pi * 12 * t), log=False)

    # *square3* updates
    if square3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        square3.frameNStart = frameN  # exact frame index
        square3.tStart = t  # local t and not account for scr refresh
        square3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square3, 'tStartRefresh')  # time at next scr refresh
        square3.setAutoDraw(True)
    # if square3.status == STARTED:
    #     # is it time to stop? (based on global clock, using actual start)
    #     if tThisFlipGlobal > square3.tStartRefresh + 3 - frameTolerance:
    #         # keep track of stop time/frame for later
    #         square3.tStop = t  # not accounting for scr refresh
    #         square3.frameNStop = frameN  # exact frame index
    #         win.timeOnFlip(square3, 'tStopRefresh')  # time at next scr refresh
    #         square3.setAutoDraw(False)
    if square3.status == STARTED:  # only update if drawing
        square3.setOpacity(sg.square(2 * np.pi * 8.57 * t), log=False)

    # *square4* updates
    if square4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        square4.frameNStart = frameN  # exact frame index
        square4.tStart = t  # local t and not account for scr refresh
        square4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square4, 'tStartRefresh')  # time at next scr refresh
        square4.setAutoDraw(True)
    # if square4.status == STARTED:
    #     # is it time to stop? (based on global clock, using actual start)
    #     if tThisFlipGlobal > square4.tStartRefresh + 3 - frameTolerance:
    #         # keep track of stop time/frame for later
    #         square4.tStop = t  # not accounting for scr refresh
    #         square4.frameNStop = frameN  # exact frame index
    #         win.timeOnFlip(square4, 'tStopRefresh')  # time at next scr refresh
    #         square4.setAutoDraw(False)
    if square4.status == STARTED:  # only update if drawing
        square4.setOpacity(sg.square(2 * np.pi * 5.45 * t), log=False)

    ##################### EACH FRAME POG ###############################
    if (frameN % int(3 * expInfo['frameRate']) == 0 and frameN != 0):
        queue_data = list(next(generator).queue)
        print("SIZE: {}".format(len(queue_data)))
        ml_data = np.asarray(queue_data)
        handler.predict(ml_data)
    elif (frameN % int(expInfo['frameRate'] / 8) == 0):
        queue_data = list(next(generator).queue)

    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

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
thisExp.addData('square1.started', square1.tStartRefresh)
thisExp.addData('square1.stopped', square1.tStopRefresh)
thisExp.addData('square2.started', square2.tStartRefresh)
thisExp.addData('square2.stopped', square2.tStopRefresh)
thisExp.addData('square3.started', square3.tStartRefresh)
thisExp.addData('square3.stopped', square3.tStopRefresh)
thisExp.addData('square4.started', square4.tStartRefresh)
thisExp.addData('square4.stopped', square4.tStopRefresh)
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
thisExp.saveAsWideText(filename + '.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
