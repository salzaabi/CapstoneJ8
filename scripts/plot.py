import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
from scipy import signal
from scipy.signal import kaiserord, lfilter, firwin, freqz, butter, filtfilt, convolve


def butter_band_targets(targets, low=0.16, high=16.0):
    for i in range(num_targets):
        for channel in channels:
            targets[i][channel] = butter_band(np.asarray(targets[i][channel]), lowcut=low, highcut=high)
    return targets

def butter_band(data, s_r=128.0, lowcut=0.16, highcut=50.0, order=5):
    # ------------------------------------------------
    # Create a butterworth bandpass filter and apply it to data.
    # ------------------------------------------------
    nyq = 0.5 * s_r
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    # data = data * 50  # amplify data
    return filtfilt(b, a, data)

def plot_time_all(data, start=0, end=129, extend_title='', show=True, save=False, name=''):
    # df plot
    fig, ax = plt.subplots(num_targets//2, 2, figsize=(12, 8), constrained_layout=True)
    for i in range(num_targets):
        for channel in channels:
            data[i][channel][start:end].plot(y=channel, grid=True, ax=ax.flatten()[i], title='Target {} Signal Over Time {}'.format(i, extend_title) if i != 8 else 'Neutral Target Signal')
        ax.flatten()[i].set_xlabel('Samples')
        ax.flatten()[i].set_ylabel('Amplitude (uV)')
        ax.flatten()[i].legend(channels)
        ax.flatten()[i].autoscale(axis='y', tight=True)
    if show:
        plt.show()
    if save:
        fig.savefig('plot_time_all{}.png'.format(name))


def plot_power_all(data, start=0, end=60, extend_title='', show=True, save=False, name=''):
    # plot power spectrum - list of df
    # use median average power spectrum
    fig, axs = plt.subplots(num_targets//2, 2, figsize=(12, 8), constrained_layout=True)
    for i in range(len(data)):
        for color, channel in enumerate(channels):
            sig = np.asarray(data[i][channel])
            freqs, pows = signal.welch(sig, 128.0, nperseg=128, average='median')
            axs.flatten()[i].plot(freqs[start:end], pows[start:end], label=channel, color=my_colors[color])
        axs.flatten()[i].set_yscale('log')
        axs.flatten()[i].grid()
        axs.flatten()[i].set_title('Target {} ({} Hz) Power Spectrum {}'.format(i, frequencies[i], extend_title))
        axs.flatten()[i].set_xlabel('Frequency (Hz)')
        axs.flatten()[i].set_ylabel('PSD (V^2/Hz)')
        axs.flatten()[i].legend()
    if show:
        plt.show()
    if save:
        fig.savefig('plot_power_all{}.png'.format(name))


if __name__ == "__main__":
    my_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    frequencies = [15.0, 12.0, 8.57, 5.45]

    # sultan data
    # dataset_name = "sultan_psychopy_recordings/eeg_psychopy_sultan_recording_" # 0 to 3
    # person = 'sultan'
    dataset_name = "recordings/eeg_peter_new_" # 0 to 3
    person = 'peter'

    num_targets = 4
    targets = [None] * num_targets
    channels = ['P7', 'O1', 'O2', 'P8'] # data channels
    for i in range(num_targets):
        targets[i] = pd.read_csv(dataset_name+str(i)+'.csv')

    # copy unfiltered data
    original_data = [None] * num_targets
    for i in range(num_targets):
        original_data[i] = pd.read_csv(dataset_name+str(i)+'.csv')

    plot_time_all(targets, extend_title='- Unfiltered', save=True, show=False, name='{}_1s_unf'.format(person))
    plot_time_all(targets, end=1000, extend_title='- Unfiltered', save=True, show=False, name='{}_1000samp_unf'.format(person))

    targets = butter_band_targets(targets, low=0.16, high=30)

    plot_time_all(targets, extend_title='- Filtered', save=True, show=False, name='{}_1s_f'.format(person))
    plot_time_all(targets, end=1000, extend_title='- Filtered', save=True, show=False, name='{}_1000samp_f'.format(person))

    plot_power_all(original_data, extend_title='(Before filtering)', save=True, show=False, name='{}_bf'.format(person)) # unfiltered
    plot_power_all(targets, extend_title='(After filtering)', save=True, show=False, name='{}_af'.format(person)) # filtered