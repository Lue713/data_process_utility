import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class TFGen(object):
    def __init__(self):
        self.raw_data_column_num = 0
        self.raw_data_row_num = 0
        self.raw_data = None
        self.fine_data = None

    def load_data(self, file_path):
        self.raw_data = pd.read_table(file_path, sep=',')
        self.raw_data_column_num = self.raw_data.shape[1]
        self.raw_data_row_num = self.raw_data.shape[0]
        index_column =[i for i in range(self.raw_data_row_num)]
        self.fine_data = pd.DataFrame(index_column, columns=['index'])
        # print(self.raw_data)
        # print(self.fine_data)

    def my_FFT(self):
        pass

    def draw_bode_plot(self):
        pass

    def diff_forward(self, input_column_name, output_column_name, order = 1):
        if order is 1:
            # raw_column_data = np.array(self.raw_data[input_column_name])
            raw_column_data = self.raw_data[input_column_name].tolist()
            diffed_data = np.diff(raw_column_data).tolist()
            diffed_data = [diffed_data[0]] + diffed_data
            # self.fine_data.insert(self.fine_data.shape[1], output_column_name, diffed_data)
            self.fine_data[output_column_name] = diffed_data
            # print(self.fine_data)
        elif order is 2:
            print('order not support yet')
        else:
            print('order not support yet')

    def diff_backward(self,column_name, order = 1):
        pass

    def show_current_data(self):
        print('raw_data:', self.raw_data.columns.values.tolist())
        print('fine_data:', self.fine_data.columns.values.tolist())

    def plot_with_cursor(self):
        pass

