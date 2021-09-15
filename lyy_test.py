import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from tf_gen import TFGen
import scipy as sp
from matplotlib import pyplot as plt

time = np.arange(0.0,2.0,0.01)
sin = np.sin(2*np.pi*time)
cos = np.cos(2*np.pi*time)
#
test_data = pd.DataFrame(time, columns = ['time'])
test_data['sin'] = sin
test_data['cos'] = cos
test_data.to_csv('data/test.csv', index = False)

tfGen_test = TFGen(0.01)
tfGen_test.load_data('./data/test.csv')
# tfGen_test.diff_forward('test1', 'test1_vel')
tfGen_test.show_current_data()
# tfGen_test.plot_with_cursor(time,[sin, cos])
# tfGen_test.plot_with_cursor(time,[time], logarithm=True)
# tfGen_test.plot_with_cursor(time,[sin, cos], subplot_num=2,snap=False)

# plt.semilogx(time, 20*np.log10(time))
# plt.plot(time, time)
# plt.show()

cplx_data, gain, phase= tfGen_test.FFT_1D('sin', 'xxx')
tfGen_test.plot_with_cursor(time,[gain, phase])



# print([[1], [1]])

