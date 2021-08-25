import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class TFGen(object):
    def __init__(self):
        pass

    def load_data(self, file_path):
        raw_data = pd.read_table(file_path, sep=',')
        print(raw_data)

    def my_FFT(self):
        pass

    def draw_bode_plot(self):
        pass

