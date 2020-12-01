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
my_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

channels = ['P7', 'O1', 'O2', 'P8']
num_targets = 4
target_pd = pd.DataFrame(columns=channels)
target_pd_list = [target_pd] * num_targets

sample_rate = 128.0
num_seconds = 100
samples = int(sample_rate * num_seconds)

mean = 0
stdev = 2
variance = stdev ** 2
a = (mean - (variance / 2))
b = ((mean * 2) - a)
# time goes from 0 to number of seconds with spacing of 1/sample_rate
# sampling frequency is 128 Hz - 100 sec of data
timeList = np.arange(0, num_seconds, 1/sample_rate)

target_freqs = [5.45, 8.57, 12.0, 15.0]

# set data for each dataframe
for i in range(num_targets):
	for channel in channels:
		white_noise = np.random.normal(mean, stdev, samples)
		noise = np.random.uniform(a, b, samples)
		drift = np.random.choice(np.arange(0.5, 5, 10)) * np.linspace(0, 10, samples)
		target_signal_channel = np.sin(2 * np.pi * target_freqs[i] * timeList) * noise + drift + white_noise
		target_pd_list[i][channel] = target_signal_channel


def plot_time_all(data, start=0, end=1000):
	# plot list of df for all channels
	fig, axs = plt.subplots(2, 2)
	for i in range(num_targets):
		for color, channel in enumerate(channels):
			data[i][channel][start:end].plot(x=timeList, y=channel, ax=axs.flatten()[i], color=my_colors[color], title='Simulated Target Freq ({} Hz) Signal Over Time'.format(target_freqs[i]))
		axs.flatten()[i].legend(channels)
		axs.flatten()[i].autoscale(axis='y', tight=True)
	plt.show()

# have to close plot before saving files.
plot_time_all(target_pd_list)

# write to files - if no directory exists, then make one
for i in range(num_targets):
	if not os.path.exists('simulated_recordings'):
		os.makedirs('simulated_recordings')
	target_pd_list[i].to_csv('simulated_recordings/simulated_target_{}.csv'.format(i))

print('done writing files.')


