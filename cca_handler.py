import pandas as pd
import numpy as np
from sklearn.cross_decomposition import CCA
# from matplotlib import pyplot as plt

from FilterClass import Filter

# TODO: optional plotting functions - separate class?
# TODO: apply filtering

class cca_handler():

    def __init__(self, controller, num_targets=4, num_seconds=3):

        self.controller = controller
        
        self.num_targets = num_targets
        self.num_seconds = num_seconds # number of seconds for a stimulus cycle

        self.sampling_rate = 128.0
        # frequencies calculated by frames/len(array) as seen in flicker_patterns.txt
        # or frequencies are set from paper we are basing our experiment from 
        # check for either 4 or 8 targets
        if self.num_targets == 8:
            self.frequencies = [32.0, 21.33, 14.22, 42.67, 16.0, 64.0, 25.6, 18.29]
        elif self.num_targets == 4:
            # up, down, right, left from paper
            # NOTE: using old csv files with these new frequencies is not valid
            self.frequencies = [5.45, 8.57, 12.0, 15.0]
        else:
            print("cca did not get a good number of targets!")

        # prediction should be targets 1 to num_targets, not 0 to num_targets - 1
        # based on command_to_keyboard action
        self.prediction = None 

        self.ref_signals = [] 
        self.getAllReferenceSignals()

        self.cca = CCA(n_components=1)

        self.fig = None
        self.ax = None
        self.plotter = None

        # self.plotting = plotting
        # if self.plotting:
        #     self.start_plot()

        self.filter_obj = Filter()
        

    # def start_plot(self):
    #     self.fig, self.ax = plt.subplots(figsize=(10 ,5))
    #     self.fig.show()

    # def plot_signals(self, data):
    #     # plot columns data
    #     self.ax.cla()
    #     for col in data.T:
    #         self.ax.plot(col)
    #     # plt.pause(0.01)
    #     self.fig.canvas.draw()


    def getAllReferenceSignals(self):
        samples = self.sampling_rate * self.num_seconds
        for freq in self.frequencies:
            self.ref_signals.append(self.generateReferenceSignal(samples, freq))
        self.ref_signals = np.asarray(self.ref_signals)


    def generateReferenceSignal(self, samples, target_freq):
        # get references for one frequency
        reference_signals = []
        t = np.arange(0, (samples/self.sampling_rate), step=1.0/self.sampling_rate)
        reference_signals.append(np.sin(np.pi*2*target_freq*t))
        reference_signals.append(np.cos(np.pi*2*target_freq*t))
        reference_signals.append(np.sin(np.pi*4*target_freq*t))
        reference_signals.append(np.cos(np.pi*4*target_freq*t))
        reference_signals = np.asarray(reference_signals)

        return reference_signals


    def findCorr(self, input_data, target_signal):
        # print('input data shape: {}'.format(input_data.shape))
        result = np.zeros((target_signal.shape)[0])
        for i in range(0, (target_signal.shape)[0]):
            self.cca.fit(input_data, np.squeeze(target_signal[i,:,:]).T)
            a, b = self.cca.transform(input_data, np.squeeze(target_signal[i,:,:]).T)
            corr = np.corrcoef(a[:,0], b[:,0])[0, 1]
            # print('correlation target {} = {}'.format(i, corr))
            result[i] = corr
        return result

    def filter(self, data):
        # perform filtering based on some function in FilterClass
        data = self.filter_obj.butter_filter(data)
        return self.filter_obj.car_filter(data)

    def predict(self, data):
        # return the prediction to the program using this command handler

        # make sure data shape and references shape are equal
        if data.T.shape != self.ref_signals[0].shape:
            print("unequal shapes: data -> {} \t ref_signals -> {}. choosing non-action.".format(data.shape, self.ref_signals[0].shape))
            return 0
        
        data = self.filter(data)
        corrs = self.findCorr(data, self.ref_signals)
        self.prediction = np.argmax(corrs)
        print("Predicted Target: {}".format(self.prediction))
        # if self.plotting:
        #     self.plot_signals(data)
            
        if self.controller is not None:
            self.command_to_keyboard_action(self.prediction + 1)
        
        return self.prediction


    def command_to_keyboard_action(self, command):
        # command 0 is no-action
        if command == 0:
            return
        elif command == 1:
            self.controller.send_command('x')
        elif command == 2:
            self.controller.send_command('up')
        elif command == 3:
            self.controller.send_command('z')
        elif command == 4:
            self.controller.send_command('left')
        elif command == 5:
            self.controller.send_command('right')
        elif command == 6:
            self.controller.send_command('start')
        elif command == 7:
            self.controller.send_command('down')
        elif command == 8:
            self.controller.send_command('select')



