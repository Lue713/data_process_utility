import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class TFGen(object):
    def __init__(self):
        pass

    def load_data(self, file_path):
        raw_data = pd.read_table(file_path, sep=',')
        print(raw_data['test1'])

    def my_FFT(self):
        pass

    def draw_bode_plot(self):
        pass

    def diff_forward(self, colum_name, order = 1):
        pass

    def diff_backward(self,column_name, order = 1):
        pass

