# live predicting window, and import csv as user input
# arrow should point to the correct input
# TODO: perhaps a square around the chosen input 
# used some parts from data_collection_window, command_handler, gaming_window

import os
from project_constants import FREQUENCY, PATTERN_LENGTH, PADDING, BASE_HEIGHT, BASE_WIDTH, ARROW_SIZE, ARROW_SCALE, \
    CHECKERBOARD_SIZE, RECORDINGS_PER_ICON, SECONDS_PER_RECORDING, COMMAND_SEND_FREQUENCY
import pandas as pd
import numpy as np
# from pyboy import PyBoy
# from pyboy.utils import WindowEvent
# import sdl2
# from command_handler import command_handler
from cca_handler import cca_handler
import ctypes
import time
import re
from psychopy import core, visual


class cca_simple_predicting_window():

    def __init__(self, recording_name='recordings/first_target_0.csv'):

        # set frame rate as (1 / desired_frame_rate)
        # self.set_update_rate(1/FREQUENCY)

        # data collection vars
        self.generator = None
        # recording data is imported from csv
        self.recording_data = []

        # length of recording data
        self.record_length = None
        self.tick = 0

        # row number index
        self.row_index = 0

        self.channels = ['O1', 'O2']

        self.display_target = None # psychopy text object
        self.target = None # number


        # ML vars
        self.command_handler = None

        # psychopy vars
        self.win = None

        self.running = False

        # set recording name
        self.recording_name = recording_name

        # import
        self.import_recording()

    def print_stage(self, stage):
        print('-'*20)
        print('{} BEGINNING'.format(stage))
        print('-'*20)

    def setup(self):
        self.print_stage("VISUALS SETUP")
        self.setup_visuals()
        self.print_stage("COMMAND HANDLER SETUP")
        self.setup_command_handler()
        print('FREQUENCY = {} \t COMMAND_SEND_FREQUENCY = {}'.format(FREQUENCY, COMMAND_SEND_FREQUENCY))
        self.running = True # ready to run 
        
    def setup_visuals(self):
        self.win = visual.Window([400, 300])
        self.display_target = visual.TextStim(self.win, text="Predicted target:")
        self.display_target.draw()
        self.win.flip()

    def setup_command_handler(self):
        # choose the desired command handler
        self.command_handler = cca_handler(None, num_targets=4, num_seconds=1)

    # def on_update(self, delta_time):
    #     # check if done
    #     if self.row_index >= self.record_length:
    #         print('-'*20)
    #         print('Done reading file. Exiting')
    #         print('-'*20)
    #         self.exit_window()
    #     # self.pyboy.tick()
    #     self.tick += 1
    #     self.tick %= FREQUENCY
    #     if self.tick % COMMAND_SEND_FREQUENCY == 0:
    #         start = time.time()
    #         self.target = self.command_handler.predict(self.get_eeg_data())
    #         self.on_draw()
    #         # print("Guess done in: {}s".format(time.time() - start))
    #         self.row_index += 128

    # def exhaust(self):
    #   next(self.generator)
    
    def on_draw(self):
        self.display_target.text = str(self.target)
        self.display_target.draw()
        self.win.flip()

    def get_eeg_data(self):
        # return np.asarray(list(next(self.generator).queue))
        # get 128 rows of recording_data
        return np.asarray(self.recording_data[self.channels][self.row_index:self.row_index + 128])


    def import_recording(self):
        # make sure name is ok
        if 'old_bad_recordings/' not in self.recording_name:
            self.recording_name = 'old_bad_recordings/' + self.recording_name
        if '.csv' not in self.recording_name:
            self.recording_name += '.csv'
        self.recording_data = pd.read_csv(self.recording_name)
        self.record_length = len(self.recording_data.index)

    def on_key_press(self, key, key_modifiers):
        actions = []
        print("KEY PRESSED: {}".format(key))

        # switch statement to create WindowEvents (button commands for PyBoy)
#       if (key == arcade.key.UP):
#           actions = [WindowEvent.PRESS_ARROW_UP, WindowEvent.RELEASE_ARROW_UP]
#       elif (key == arcade.key.DOWN):
#           actions = [WindowEvent.PRESS_ARROW_DOWN, WindowEvent.RELEASE_ARROW_DOWN]
#       elif (key == arcade.key.LEFT):
#           actions = [WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT]
#       elif (key == arcade.key.RIGHT):
#           actions = [WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT]
#       elif (key == arcade.key.Z):
#           actions = [WindowEvent.PRESS_BUTTON_B, WindowEvent.RELEASE_BUTTON_B]
#       elif (key == arcade.key.X):
#           actions = [WindowEvent.PRESS_BUTTON_A, WindowEvent.RELEASE_BUTTON_A]
#       elif (key == arcade.key.ENTER):
#           actions = [WindowEvent.PRESS_BUTTON_SELECT, WindowEvent.RELEASE_BUTTON_SELECT]
#       elif (key == arcade.key.RSHIFT):
#           actions = [WindowEvent.PRESS_BUTTON_START, WindowEvent.RELEASE_BUTTON_START]

        # if actions list isn't empty, send commands to pyboy and tick the pyboy window to process each command
#       if actions:
#           for action in actions:
#               self.pyboy.send_input(WindowEvent(action))
#               self.pyboy.tick()

    def exit_window(self):
        print('-'*20)
        print('Done reading file. Exiting')
        print('-'*20)
        self.running = False
        self.win.close()
        core.quit()
        exit()

    def run(self):
        while self.running:
            
            if self.row_index >= self.record_length:
                # done and exit
                self.exit_window()

            core.wait(1.0)
            self.target = self.command_handler.predict(self.get_eeg_data())
            self.on_draw()
            # print("Guess done in: {}s".format(time.time() - start))
            self.row_index += 128


if __name__ == "__main__":
    window = cca_simple_predicting_window('old_bad_recordings/first_target_1')
    window.setup()
    window.run()