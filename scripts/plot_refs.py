from cca_handler import cca_handler
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == "__main__":
	cca = cca_handler(num_targets=4, num_seconds=1)

	cca.plot_reference_signals(show=True, save=True, name='4_target')