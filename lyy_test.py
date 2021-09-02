from tf_gen import TFGen

tfGen = TFGen()
tfGen.load_data('./data/test.csv')
tfGen.diff_forward('test1', 'test1_vel')
tfGen.show_current_data()

import matplotlib.pyplot as plt
import numpy as np

# class Cursor(object):
#     def __init__(self, ax):
#         self.ax = ax
#         self.lx = ax.axhline(color='k')  # the horiz line
#         self.ly = ax.axvline(color='k')  # the vert line
#
#         # text location in axes coords
#         self.txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)
#
#     def mouse_move(self, event):
#         if not event.inaxes:
#             return
#
#         x, y = event.xdata, event.ydata
#         # update the line positions
#         self.lx.set_ydata(y)
#         self.ly.set_xdata(x)
#
#         self.txt.set_text('x=%1.11f\ny=%1.11f' % (x, y))
#         plt.draw()
#
# class SnaptoCursor(object):
#     """
#     Like Cursor but the crosshair snaps to the nearest x,y point
#     For simplicity, I'm assuming x is sorted
#     """
#
#     def __init__(self, ax, x, y):
#         self.ax = ax
#         self.lx = ax.axhline(color='k')  # the horiz line
#         self.ly = ax.axvline(color='k')  # the vert line
#         self.x = x
#         self.y = y
#         # text location in axes coords
#         self.txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)
#
#     def mouse_move(self, event):
#
#         if not event.inaxes:
#             return
#
#         x, y = event.xdata, event.ydata
#
#         indx = min(np.searchsorted(self.x, [x])[0], len(self.x) - 1)
#         x = self.x[indx]
#         y = self.y[indx]
#         # update the line positions
#         self.lx.set_ydata(y)
#         self.ly.set_xdata(x)
#
#         self.txt.set_text('x=%1.11f\ny=%1.11f' % (x, y))
#         print('x=%1.11f\ny=%1.11f' % (x, y))
#         plt.draw()
#
# t = np.arange(0.0,1.0,0.01)
# s = np.sin(2*np.pi*t)
# #  make line red
# fig, ax = plt.subplots()
# plt.rcParams['lines.color'] = 'r'
# ax.plot(t,s)
# # plt.show()
# #
# c = np.cos(2*np.pi*t)
# #
# # #make line thick
# plt.rcParams['lines.linewidth'] = '1'
# plt.plot(t,c)
# plt.xlabel('t')
# plt.ylabel('cos(2*pi*t)')
# plt.title('Plot test')
#
# cursor = Cursor(ax)
# # cursor = SnaptoCursor(ax, t, s)
# plt.connect('motion_notify_event', cursor.mouse_move)
# plt.show()

