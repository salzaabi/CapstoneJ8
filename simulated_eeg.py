# generate noisy stimulus data for either 1, 2, or 3 seconds

# Notes:
# - no TIME column
# - no DC offset like Emotiv's - Values are centered around zero. 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import os
from scipy import signal
my_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:cyan', 'tab:gray']


class simulated_eeg():

	def __init__(self, num_targets=8, num_seconds=3):
		self.num_targets = num_targets
		self.channels = ['P7', 'O1', 'O2', 'P8']
		if self.num_targets == 4:
			self.target_freqs = np.asarray([15.0, 12.0, 8.57, 5.45])
		elif self.num_targets == 8:
			self.target_freqs = np.asarray([43.0, 37.0, 29.0, 21.0, 17.0, 11.0, 8.0, 5.0])
		else:
			print("simulated_eeg did not get a good target number.")
		self.second_harmonic = self.target_freqs * 2
		self.num_seconds = num_seconds
		self.sample_rate = 128.0
		self.samples = int(self.num_seconds * self.sample_rate)
		self.timeList = np.arange(0, self.num_seconds, 1/self.sample_rate)
		self.targets = []
		for i in range(self.num_targets + 1):
			# target 0 is non-action
			self.targets.append(pd.DataFrame(columns=self.channels))

		self.less_noise = False # default

		self.generate_all_data()

	def generate_all_data(self):
		for target in range(self.num_targets + 1):
			self.generate_one_target(target)


	def white_noise(self, mean, stdev):
		return np.random.normal(mean, stdev, self.samples)

	def band_limited_noise(self, min_freq, max_freq):
		freqs = np.arange(min_freq, max_freq, 0.1)
		phases = np.random.rand(len(freqs)) * 2 * np.pi
		signals = [np.sin(2*np.pi*freq*self.timeList+angle) for freq, angle in zip(freqs, phases)]
		# print('size {} x shape {}'.format(len(signals), signals[0].shape))
		signal = sum(signals)
		signal /= np.max(signal)
		return signal

	def generate_one_target(self, target):
		# target 0 is non-action, target 1-8 will access this class's 0-7 signals.
		if self.less_noise:
			stdev = 0
			stdev2 = 1
		else:
			stdev = 2
			stdev2 = 2

		# all_channel_random = self.white_noise(0, stdev) # big random across all channels
		all_channel_random = self.white_noise(0, stdev2)
		if not self.less_noise:
			all_channel_random += 0.25 * self.band_limited_noise(0.01, 0.16)
		for channel in self.channels:
			white_noise = self.white_noise(0, stdev2/2) # small random across each channel - do always
			if not self.less_noise:
				white_noise += 0.25 * self.band_limited_noise(0.1, 1)
			# white_noise = 0.5 * self.band_limited_noise(0.1, 1.5)
			multiply_noise = self.white_noise(1, stdev/2)
			if target == 0:
				# non-action
				signal = 0
				sec_signal = 0
			else:
				signal = np.sin(2 * np.pi * self.target_freqs[target - 1] * self.timeList)
				sec_signal = 0.3 * np.sin(2 * np.pi * self.second_harmonic[target - 1] * self.timeList)
			# if not self.less_noise:
			# 	signal *= 0.5
			# 	sec_signal *= 0.5

			target_signal_channel = signal * multiply_noise + white_noise + all_channel_random

			sec_mul_noise = self.white_noise(1, stdev/4)
			sec_add_noise = 0.3 * self.white_noise(0, stdev/4)
			second_harmonic_signal_channel = sec_signal * sec_mul_noise + sec_add_noise

			self.targets[target][channel] = target_signal_channel + second_harmonic_signal_channel


	def plot_time_all(self, start=0, end=129, save=True, folder='', show=True):
		fig, axs = plt.subplots(self.num_targets//2, 2, figsize=(15, 10), constrained_layout=True)
		for i in range(self.num_targets):
			for color, channel in enumerate(self.channels):
				self.targets[i + 1][channel][start:end].plot(x=self.timeList, y=channel, ax=axs.flatten()[i], color=my_colors[color], title='Simulated Target {} ({} Hz) Signal Over Time'.format(i, self.target_freqs[i]))
			axs.flatten()[i].set_xlabel('Samples')
			axs.flatten()[i].set_ylabel('Amplitude (uV)')
			axs.flatten()[i].legend(self.channels)
			axs.flatten()[i].autoscale(axis='y', tight=True)
		if show:
			plt.show()
		if save:
			if folder:
				fig.savefig('simulated_recordings/{}/simulated_1s_plots.png'.format(folder))
			else:
				fig.savefig('simulated_recordings/simulated_1s_plots.png')
			print('time plots saved.')


	def plot_power_all(self, start=0, end=65, save=True, folder='', show=True):
		# plot power spectrum - list of df
		# use median average power spectrum
		fig, axs = plt.subplots(self.num_targets//2, 2, figsize=(12, 8), constrained_layout=True)
		for i in range(self.num_targets):
			for color, channel in enumerate(self.channels):
				sig = np.asarray(self.targets[i + 1][channel])
				freqs, pows = signal.welch(sig, 128.0, nperseg=128, average='median')
				axs.flatten()[i].plot(freqs, pows, label=channel, color=my_colors[color])
			axs.flatten()[i].set_yscale('log')
			axs.flatten()[i].set_title('Target {} ({} Hz) Power Spectrum'.format(i, self.target_freqs[i]))
			axs.flatten()[i].set_xlabel('Frequency (Hz)')
			axs.flatten()[i].set_ylabel('PSD (V^2/Hz)')
			axs.flatten()[i].legend()
		if show:
			plt.show()
		if save:
			if folder:
				fig.savefig('simulated_recordings/{}/simulated_power_plots.png'.format(folder))
			else:
				fig.savefig('simulated_recordings/simulated_power_plots.png')
			print('power plots saved.')

	def save_data(self, folder=''):
		# save each target as csv
		# if no directory exists, then make one

		# if name is supplied, save to a specific folder in simulated_recordings
		folder_exist = os.path.exists('simulated_recordings')
		if not folder_exist:
			os.makedirs('simulated_recordings')
		if folder_exist and not os.path.exists('simulated_recordings/{}'.format(folder)):
			os.makedirs('simulated_recordings/{}'.format(folder))

		# then, save plots
		self.plot_time_all(folder=folder, show=False)
		self.plot_power_all(folder=folder, show=False)

		# then, save data
		for target in range(1, self.num_targets + 1):
			if folder:
				self.targets[target].to_csv('simulated_recordings/{}/simulated_target_{}.csv'.format(folder, target - 1))
			else:
				self.targets[target].to_csv('simulated_recordings/simulated_target_{}.csv'.format(target - 1))
		print('done writing files.')



	def get_signals(self, target):
		# targets are from 1 to num_targets. 0 is non-action
		self.generate_one_target(target)
		return np.asarray(self.targets[target][self.channels])


