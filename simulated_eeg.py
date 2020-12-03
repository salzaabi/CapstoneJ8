# simulate eeg 

# Notes:
# - no TIME column
# - have to close plot before saving files. Verify plot when running
# - no DC offset like Emotiv's - Values are mostly centered around zero. 


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
plt.style.use('ggplot')


def plot_time_all(data, start=0, end=1000, save=True):
	# plot list of df for all channels
	fig, axs = plt.subplots(2, 2, figsize=(15, 10))
	for i in range(num_targets):
		for color, channel in enumerate(channels):
			data[i][channel][start:end].plot(x=timeList, y=channel, ax=axs.flatten()[i], color=my_colors[color], title='Simulated Target {} ({} Hz) Signal Over Time'.format(i, target_freqs[i]))
		axs.flatten()[i].legend(channels)
		axs.flatten()[i].autoscale(axis='y', tight=True)
	plt.show()
	if save:
		fig.savefig('simulated_recordings/simulated_1s_plots.png')
		print('plots saved.')


if __name__ == "__main__":
	if not os.path.exists('simulated_recordings'):
				os.makedirs('simulated_recordings')
	my_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

	channels = ['P7', 'O1', 'O2', 'P8']
	df_cols = ['Counter', 'P7', 'O1', 'O2', 'P8']
	num_targets = 4
	target_df_list = []
	for i in range(num_targets):
		target_df = pd.DataFrame(columns=df_cols)
		target_df_list.append(target_df)

	sample_rate = 128.0
	num_seconds = 100
	samples = int(sample_rate * num_seconds)

	mean = 0
	stdev = 2
	variance = stdev ** 2
	# time goes from 0 to number of seconds with spacing of 1/sample_rate
	# sampling frequency is 128 Hz - 100 sec of data
	timeList = np.arange(0, num_seconds, 1/sample_rate)

	target_freqs = [15.0, 12.0, 8.57, 5.45]
	second_harmonic = [30.0, 24.0, 17.14, 10.9]

	# control
	en_drift = True
	en_white_noise = True
	en_multiply_noise = True

	en_write = True

	# set data for each dataframe
	# big randomness for all channels,  small randomness for each channel
	for i in range(num_targets):
		all_channel_random = np.random.normal(0, stdev*2, samples) # big random
		for channel in channels:
			if en_white_noise:
				white_noise = np.random.normal(0, stdev/2, samples) # small random
			else:
				white_noise = 0
			if en_multiply_noise:
				multiply_noise = np.random.uniform(0.2, 3, samples)
			else:
				multiply_noise = 1.0
			if en_drift:
				drift = np.random.choice(np.arange(0.5, 5, 10)) * np.linspace(0, 10, samples)
			else:
				drift = 0
			target_signal_channel = np.sin(2 * np.pi * target_freqs[i] * timeList) * multiply_noise + drift + white_noise + all_channel_random
			sec_mul_noise = np.random.uniform(0.5, 1.5, samples)
			sec_add_noise = np.random.normal(0, stdev/8, samples)
			second_harmonic_signal_channel = 0.2 * np.sin(2 * np.pi * second_harmonic[i] * timeList) * sec_mul_noise + sec_add_noise
			target_df_list[i][channel] = target_signal_channel + second_harmonic_signal_channel

	# have to close plot before saving files.
	plot_time_all(target_df_list, start=0, end=128)

	# write to files - if no directory exists, then make one
	if en_write:
		for i in range(num_targets):
			target_df_list[i].to_csv('simulated_recordings/simulated_target_{}.csv'.format(i))
		print('done writing files.')
	else:
		print('done. not writing files.')


