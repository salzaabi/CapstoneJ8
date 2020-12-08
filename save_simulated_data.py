from simulated_eeg import simulated_eeg

if __name__ == "__main__":

	# generate data with less_noise flag off and then on

	# eeg = simulated_eeg(num_targets=8, num_seconds=100)
	# eeg.save_data(folder='new_noise')

	# eeg.less_noise = True  
	# eeg.generate_all_data()
	# eeg.save_data(folder='new_less_noise')

	eeg = simulated_eeg(num_targets=8, num_seconds=100)
	eeg.save_data(folder='test')

	# eeg = simulated_eeg(num_targets=4, num_seconds=3)
	# eeg.less_noise = True
	# eeg.generate_all_data()
	# eeg.save_data(folder='four_targets_less_noise')