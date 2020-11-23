#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.6),
    on November 22, 2020, at 15:38
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

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
from psychopy.hardware import emotiv

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.6'
expName = 'offline'  # from the Builder filename that created this script
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
                                 originPath='C:\\Users\\sulta\\OneDrive\\Desktop\\Capstone Project PsychoPy\\offline.py',
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
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "connect"
connectClock = core.Clock()
from cortex import Cortex

cortex = Cortex(None)
cortex.do_prepare_steps()
print("prepare steps done")

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
                               text='Welcome, this is the instructions!',
                               font='Arial',
                               pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                               color='white', colorSpace='rgb', opacity=1,
                               languageStyle='LTR',
                               depth=0.0);
ready = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank_img = visual.ImageStim(
    win=win,
    name='blank_img',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
pause = visual.TextStim(win=win, name='pause',
                        text='PAUSE',
                        font='Arial',
                        pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                        color='white', colorSpace='rgb', opacity=1,
                        languageStyle='LTR',
                        depth=0.0);
indicate1 = visual.Rect(
    win=win, name='indicate1', units='pix',
    width=(200, 200)[0], height=(200, 200)[1],
    ori=0, pos=(0, 400),
    lineWidth=1, lineColor=[1, 0, 0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
indcate2 = visual.Rect(
    win=win, name='indcate2', units='pix',
    width=(200, 200)[0], height=(200, 200)[1],
    ori=0, pos=(-400, 0),
    lineWidth=1, lineColor=[1, 0, 0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
indcate3 = visual.Rect(
    win=win, name='indcate3', units='pix',
    width=(200, 200)[0], height=(200, 200)[1],
    ori=0, pos=(400, 0),
    lineWidth=1, lineColor=[1, 0, 0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
indicate4 = visual.Rect(
    win=win, name='indicate4', units='pix',
    width=(200, 200)[0], height=(200, 200)[1],
    ori=0, pos=(0, -400),
    lineWidth=1, lineColor=[1, 0, 0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
from scipy import signal as sg

# Fs = 44100
# f = 440
# sample = Fs / f
# speed = 200  # Speed of flicker
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

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank_img = visual.ImageStim(
    win=win,
    name='blank_img',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "connect"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
connectComponents = []
for thisComponent in connectComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
connectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "connect"-------
while continueRoutine:
    # get current time
    t = connectClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=connectClock)
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
    for thisComponent in connectComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "connect"-------
for thisComponent in connectComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "connect" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
ready.keys = []
ready.rt = []
_ready_allKeys = []
# keep track of which components have finished
instrComponents = [instructions, ready]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)

    # *ready* updates
    waitOnFlip = False
    if ready.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        ready.frameNStart = frameN  # exact frame index
        ready.tStart = t  # local t and not account for scr refresh
        ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        ready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready.status == STARTED and not waitOnFlip:
        theseKeys = ready.getKeys(keyList=None, waitRelease=False)
        _ready_allKeys.extend(theseKeys)
        if len(_ready_allKeys):
            ready.keys = _ready_allKeys[-1].name  # just the last key pressed
            ready.rt = _ready_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# check responses
if ready.keys in ['', [], None]:  # No response was made
    ready.keys = None
thisExp.addData('ready.keys', ready.keys)
if ready.keys != None:  # we had a response
    thisExp.addData('ready.rt', ready.rt)
thisExp.addData('ready.started', ready.tStartRefresh)
thisExp.addData('ready.stopped', ready.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='sequential',
                           extraInfo=expInfo, originPath=-1,
                           trialList=[None],
                           seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [blank_img]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *blank_img* updates
        if blank_img.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            blank_img.frameNStart = frameN  # exact frame index
            blank_img.tStart = t  # local t and not account for scr refresh
            blank_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_img, 'tStartRefresh')  # time at next scr refresh
            blank_img.setAutoDraw(True)
        if blank_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_img.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                blank_img.tStop = t  # not accounting for scr refresh
                blank_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_img, 'tStopRefresh')  # time at next scr refresh
                blank_img.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('blank_img.started', blank_img.tStartRefresh)
    trials.addData('blank_img.stopped', blank_img.tStopRefresh)

    # set up handler to look after randomisation of conditions etc
    circles = data.TrialHandler(nReps=1, method='random',
                                extraInfo=expInfo, originPath=-1,
                                trialList=data.importConditions('conditions.xlsx'),
                                seed=None, name='circles')
    thisExp.addLoop(circles)  # add the loop to the experiment
    thisCircle = circles.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCircle.rgb)
    if thisCircle != None:
        for paramName in thisCircle:
            exec('{} = thisCircle[paramName]'.format(paramName))

    for thisCircle in circles:
        currentLoop = circles
        # abbreviate parameter names if possible (e.g. rgb = thisCircle.rgb)
        if thisCircle != None:
            for paramName in thisCircle:
                exec('{} = thisCircle[paramName]'.format(paramName))

        # ------Prepare to start Routine "ISI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        indicate1.setFillColor(color1)
        indcate2.setFillColor(color2)
        indcate3.setFillColor(color3)
        indicate4.setFillColor(color4)
        # keep track of which components have finished
        ISIComponents = [pause, indicate1, indcate2, indcate3, indicate4]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *pause* updates
            if pause.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                pause.frameNStart = frameN  # exact frame index
                pause.tStart = t  # local t and not account for scr refresh
                pause.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pause, 'tStartRefresh')  # time at next scr refresh
                pause.setAutoDraw(True)
            if pause.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pause.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    pause.tStop = t  # not accounting for scr refresh
                    pause.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pause, 'tStopRefresh')  # time at next scr refresh
                    pause.setAutoDraw(False)

            # *indicate1* updates
            if indicate1.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
                # keep track of start time/frame for later
                indicate1.frameNStart = frameN  # exact frame index
                indicate1.tStart = t  # local t and not account for scr refresh
                indicate1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(indicate1, 'tStartRefresh')  # time at next scr refresh
                indicate1.setAutoDraw(True)
            if indicate1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > indicate1.tStartRefresh + 1 - frameTolerance:
                    # keep track of stop time/frame for later
                    indicate1.tStop = t  # not accounting for scr refresh
                    indicate1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(indicate1, 'tStopRefresh')  # time at next scr refresh
                    indicate1.setAutoDraw(False)

            # *indcate2* updates
            if indcate2.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
                # keep track of start time/frame for later
                indcate2.frameNStart = frameN  # exact frame index
                indcate2.tStart = t  # local t and not account for scr refresh
                indcate2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(indcate2, 'tStartRefresh')  # time at next scr refresh
                indcate2.setAutoDraw(True)
            if indcate2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > indcate2.tStartRefresh + 1 - frameTolerance:
                    # keep track of stop time/frame for later
                    indcate2.tStop = t  # not accounting for scr refresh
                    indcate2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(indcate2, 'tStopRefresh')  # time at next scr refresh
                    indcate2.setAutoDraw(False)

            # *indcate3* updates
            if indcate3.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
                # keep track of start time/frame for later
                indcate3.frameNStart = frameN  # exact frame index
                indcate3.tStart = t  # local t and not account for scr refresh
                indcate3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(indcate3, 'tStartRefresh')  # time at next scr refresh
                indcate3.setAutoDraw(True)
            if indcate3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > indcate3.tStartRefresh + 1 - frameTolerance:
                    # keep track of stop time/frame for later
                    indcate3.tStop = t  # not accounting for scr refresh
                    indcate3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(indcate3, 'tStopRefresh')  # time at next scr refresh
                    indcate3.setAutoDraw(False)

            # *indicate4* updates
            if indicate4.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
                # keep track of start time/frame for later
                indicate4.frameNStart = frameN  # exact frame index
                indicate4.tStart = t  # local t and not account for scr refresh
                indicate4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(indicate4, 'tStartRefresh')  # time at next scr refresh
                indicate4.setAutoDraw(True)
            if indicate4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > indicate4.tStartRefresh + 1 - frameTolerance:
                    # keep track of stop time/frame for later
                    indicate4.tStop = t  # not accounting for scr refresh
                    indicate4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(indicate4, 'tStopRefresh')  # time at next scr refresh
                    indicate4.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        circles.addData('pause.started', pause.tStartRefresh)
        circles.addData('pause.stopped', pause.tStopRefresh)
        circles.addData('indicate1.started', indicate1.tStartRefresh)
        circles.addData('indicate1.stopped', indicate1.tStopRefresh)
        circles.addData('indcate2.started', indcate2.tStartRefresh)
        circles.addData('indcate2.stopped', indcate2.tStopRefresh)
        circles.addData('indcate3.started', indcate3.tStartRefresh)
        circles.addData('indcate3.stopped', indcate3.tStopRefresh)
        circles.addData('indicate4.started', indicate4.tStartRefresh)
        circles.addData('indicate4.stopped', indicate4.tStopRefresh)

        # ------Prepare to start Routine "stimuli"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stimuliComponents = [square1, square2, square3, square4]
        for thisComponent in stimuliComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "stimuli"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimuliClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimuliClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *square1* updates
            if square1.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
                # keep track of start time/frame for later
                square1.frameNStart = frameN  # exact frame index
                square1.tStart = t  # local t and not account for scr refresh
                square1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square1, 'tStartRefresh')  # time at next scr refresh
                square1.setAutoDraw(True)
            if square1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square1.tStartRefresh + 3 - frameTolerance:
                    # keep track of stop time/frame for later
                    square1.tStop = t  # not accounting for scr refresh
                    square1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square1, 'tStopRefresh')  # time at next scr refresh
                    square1.setAutoDraw(False)
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
            if square2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square2.tStartRefresh + 3 - frameTolerance:
                    # keep track of stop time/frame for later
                    square2.tStop = t  # not accounting for scr refresh
                    square2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square2, 'tStopRefresh')  # time at next scr refresh
                    square2.setAutoDraw(False)
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
            if square3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square3.tStartRefresh + 3 - frameTolerance:
                    # keep track of stop time/frame for later
                    square3.tStop = t  # not accounting for scr refresh
                    square3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square3, 'tStopRefresh')  # time at next scr refresh
                    square3.setAutoDraw(False)
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
            if square4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square4.tStartRefresh + 3 - frameTolerance:
                    # keep track of stop time/frame for later
                    square4.tStop = t  # not accounting for scr refresh
                    square4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square4, 'tStopRefresh')  # time at next scr refresh
                    square4.setAutoDraw(False)
            if square4.status == STARTED:  # only update if drawing
                square4.setOpacity(sg.square(2 * np.pi * 5.45 * t), log=False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimuliComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "stimuli"-------
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        circles.addData('square1.started', square1.tStartRefresh)
        circles.addData('square1.stopped', square1.tStopRefresh)
        circles.addData('square2.started', square2.tStartRefresh)
        circles.addData('square2.stopped', square2.tStopRefresh)
        circles.addData('square3.started', square3.tStartRefresh)
        circles.addData('square3.stopped', square3.tStopRefresh)
        circles.addData('square4.started', square4.tStartRefresh)
        circles.addData('square4.stopped', square4.tStopRefresh)
        thisExp.nextEntry()

    # completed 1 repeats of 'circles'

    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [blank_img]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *blank_img* updates
        if blank_img.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            blank_img.frameNStart = frameN  # exact frame index
            blank_img.tStart = t  # local t and not account for scr refresh
            blank_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_img, 'tStartRefresh')  # time at next scr refresh
            blank_img.setAutoDraw(True)
        if blank_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_img.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                blank_img.tStop = t  # not accounting for scr refresh
                blank_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_img, 'tStopRefresh')  # time at next scr refresh
                blank_img.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('blank_img.started', blank_img.tStartRefresh)
    trials.addData('blank_img.stopped', blank_img.tStopRefresh)
    thisExp.nextEntry()

# completed 3 repeats of 'trials'


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
