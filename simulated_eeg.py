# simulate eeg 

# Notes:
# - no TIME column
# - have to close plot before saving files. Verify plot when running
# - no DC offset like Emotiv's - Values are centered around zero. 


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy import signal
plt.style.use('ggplot')

# turn save to True if you want to keep the generated data
save = True

my_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:cyan', 'tab:gray']
channels = ['P7', 'O1', 'O2', 'P8']
num_targets = 8
# target_freqs = np.asarray([15.0, 12.0, 8.57, 5.45])
# target_freqs = np.asarray([29.0, 23.0, 19.0, 17.0, 13.0, 11.0, 7.0, 5.0])
target_freqs = np.asarray([43.0, 37.0, 29.0, 21.0, 17.0, 11.0, 8.0, 5.0])

sample_rate = 128.0
num_seconds = 100
samples = int(sample_rate * num_seconds)
timeList = np.arange(0, num_seconds, 1/sample_rate)


def plot_time_all(data, start=0, end=1000):
	# plot list of df for all channels
	fig, axs = plt.subplots(num_targets//2, 2, figsize=(15, 10), constrained_layout=True)
	for i in range(num_targets):
		for color, channel in enumerate(channels):
			data[i][channel][start:end].plot(x=timeList, y=channel, ax=axs.flatten()[i], color=my_colors[color], title='Simulated Target {} ({} Hz) Signal Over Time'.format(i, target_freqs[i]))
		axs.flatten()[i].legend(channels)
		axs.flatten()[i].autoscale(axis='y', tight=True)
	plt.show()
	if save:
		fig.savefig('simulated_recordings/simulated_1s_plots.png')
		print('time plots saved.')

def plot_power_all(data):
	# plot power spectrum - list of df
	# use median average power spectrum
	fig, axs = plt.subplots(4, 2, figsize=(12, 8), constrained_layout=True)
	for i in range(len(data)):
		for color, channel in enumerate(channels):
			sig = np.asarray(data[i][channel])
			freqs, pows = signal.welch(sig, 128.0, nperseg=128, average='median')
			axs.flatten()[i].plot(freqs, pows, label=channel, color=my_colors[color])
		axs.flatten()[i].set_yscale('log')
		axs.flatten()[i].set_title('Target {} ({} Hz) Power Spectrum'.format(i, target_freqs[i]))
		axs.flatten()[i].set_xlabel('Frequency (Hz)')
		axs.flatten()[i].set_ylabel('PSD (V^2/Hz)')
		axs.flatten()[i].legend()
	plt.show()
	if save:
		fig.savefig('simulated_recordings/simulated_power_plots.png')
		print('power plots saved.')


# if no directory exists, then make one
if save and not os.path.exists('simulated_recordings'):
			os.makedirs('simulated_recordings')




df_cols = ['Counter', 'P7', 'O1', 'O2', 'P8']
target_df_list = []
for i in range(num_targets):
	target_df = pd.DataFrame(columns=df_cols)
	target_df['Counter'] = [i % sample_rate for i in range(samples)]
	target_df_list.append(target_df)

mean = 0
stdev = 2
variance = stdev ** 2

second_harmonic = target_freqs * 2

# noise control
less_noise = False

# set data for each dataframe
# big randomness for all channels,  small randomness for each channel
for i in range(num_targets):
	all_channel_random = np.random.normal(0, stdev*2, samples) # big random
	for channel in channels:
		white_noise = np.random.normal(0, stdev/2, samples) # small random
		if not less_noise:
			multiply_noise = np.random.uniform(0.2, 3, samples)
		else:
			multiply_noise = 1.0
		# drift = np.random.choice(np.arange(0.5, 5, 10)) * np.linspace(0, 10, samples)
		target_signal_channel = np.sin(2 * np.pi * target_freqs[i] * timeList) * multiply_noise + white_noise + all_channel_random
		if not less_noise:
			sec_mul_noise = np.random.uniform(0.5, 1.5, samples)
			sec_add_noise = np.random.normal(0, stdev/8, samples)
		else:
			sec_mul_noise = 1.0
			sec_add_noise = 0
		second_harmonic_signal_channel = 0.5 * np.sin(2 * np.pi * second_harmonic[i] * timeList) * sec_mul_noise + sec_add_noise
		target_df_list[i][channel] = target_signal_channel + second_harmonic_signal_channel

# have to close plot before saving files.
plot_time_all(target_df_list, start=0, end=128)

plot_power_all(target_df_list)

if save:
	for i in range(num_targets):
		target_df_list[i].to_csv('simulated_recordings/simulated_target_{}.csv'.format(i))
	print('done writing files.')
else:
	print('done. not writing files.')


