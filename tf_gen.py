import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class TFGen(object):
    def __init__(self):
        self.all_data = {}

    def load_data(self, file_path):
        self.all_data['raw_data'] = pd.read_table(file_path, sep=',')
        index_column =[i for i in range(self.all_data['raw_data'].shape[0])]
        self.all_data['processed_data'] = pd.DataFrame(index_column, columns=['index'])
        # print(self.all_data['processed_data'])

    def my_FFT(self):
        pass

    def draw_bode_plot(self):
        pass

    def diff_forward(self, input_column_name, output_column_name, order = 1):
        raw_data = self.all_data['raw_data']
        processed_data = self.all_data['processed_data']

        if order is 1:
            raw_column_data = raw_data[input_column_name].tolist()
            diffed_data = np.diff(raw_column_data).tolist()
            diffed_data = [diffed_data[0]] + diffed_data
            # self.fine_data.insert(self.fine_data.shape[1], output_column_name, diffed_data)
            processed_data[output_column_name] = diffed_data
            # print(self.fine_data)
        elif order is 2:
            print('not support yet')
        else:
            print('not support yet')

        self.all_data['processed_data'] = processed_data

    def show_current_data(self, show_data = False):
        data_key_list = list(self.all_data)
        for name in data_key_list:
            print(name,':')
            if show_data:
                print(self.all_data[name],'\n')
            else:
                print(self.all_data[name].columns.values.tolist())

    def plot_with_cursor(self, x_data, y_datas, subplot_num = 1, snap = True):
        fig, ax = plt.subplots(subplot_num)
        # plt.figure()
        plt.rcParams['lines.linewidth'] = '1'
        cursor_list = []
        for i in range(subplot_num):
            ax[i].plot(x_data, y_datas[i])
            ax[i].grid()
            if snap:
                cursor_list += [SnaptoCursor(ax[i], x_data, y_datas[i])]
            else:
                cursor_list += [Cursor(ax[i])]
            plt.connect('motion_notify_event', cursor_list[i].mouse_move)
        plt.show()

class Cursor(object):
    def __init__(self, ax):
        self.ax = ax
        self.lx = ax.axhline(color='k')  # the horiz line
        self.ly = ax.axvline(color='k')  # the vert line

        # text location in axes coords
        self.txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)

    def mouse_move(self, event):
        if not event.inaxes:
            return

        x, y = event.xdata, event.ydata
        # update the line positions
        self.lx.set_ydata(y)
        self.ly.set_xdata(x)

        self.txt.set_text('x=%1.11f\ny=%1.11f' % (x, y))
        plt.draw()

class SnaptoCursor(object):
    """
    Like Cursor but the crosshair snaps to the nearest x,y point
    For simplicity, I'm assuming x is sorted
    """

    def __init__(self, ax, x, y):
        self.ax = ax
        self.lx = ax.axhline(color='k')  # the horiz line
        self.ly = ax.axvline(color='k')  # the vert line
        self.x = x
        self.y = y
        # text location in axes coords
        self.txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)

    def mouse_move(self, event):
        if not event.inaxes:
            return

        x, y = event.xdata, event.ydata
        indx = min(np.searchsorted(self.x, [x])[0], len(self.x) - 1)

        x = self.x[indx]
        y = self.y[indx]
        # update the line positions
        self.lx.set_ydata(y)
        self.ly.set_xdata(x)

        self.txt.set_text('x=%1.11f\ny=%1.11f' % (x, y))
        # print('x=%1.11f\ny=%1.11f' % (x, y))
        plt.draw()