# simulate eeg 
# generate noisy stimulus data for either 1, 2, or 3 seconds

# Notes:
# - no TIME column
# - have to close plot before saving files. Verify plot when running
# - no DC offset like Emotiv's - Values are centered around zero. 


import numpy as np
import pandas as pd

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

		self.less_noise = False
		self.stdev = 2
		self.variance = self.stdev ** 2

		for target in range(self.num_targets + 1):
			self.generate_one_target(target)

	def generate_one_target(self, target):
		# target 0 is non-action
		if self.less_noise:
			all_channel_random = np.random.normal(0, self.stdev, self.samples) # big random across all channels
		else:
			all_channel_random = np.random.normal(0, self.stdev*2, self.samples)
		for channel in self.channels:
			if self.less_noise:
				white_noise = np.random.normal(0, self.stdev/4, self.samples) # small random across each channel
			else:
				white_noise = np.random.normal(0, self.stdev/2, self.samples)
			if self.less_noise:
				multiply_noise = 1.0
			else:
				multiply_noise = np.random.uniform(0.2, 3, self.samples)
			if target == 0:
				# non-action
				signal = 0
				sec_signal = 0
			else:
				signal = np.sin(2 * np.pi * self.target_freqs[target - 1] * self.timeList)
				sec_signal = 0.3 * np.sin(2 * np.pi * self.second_harmonic[target - 1] * self.timeList)
			target_signal_channel = signal * multiply_noise + white_noise + all_channel_random
			if self.less_noise:
				sec_mul_noise = 1.0
				sec_add_noise = 0
			else:
				sec_mul_noise = np.random.uniform(0.5, 1.5, self.samples)
				sec_add_noise = np.random.normal(0, self.stdev/8, self.samples)
			second_harmonic_signal_channel = sec_signal * sec_mul_noise + sec_add_noise
			self.targets[target][channel] = target_signal_channel + second_harmonic_signal_channel


	def get_signals(self, target):
		# targets are from 1 to num_targets. 0 is non-action
		self.generate_one_target(target)
		return np.asarray(self.targets[target][self.channels])


