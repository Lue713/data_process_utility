import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from tf_gen import TFGen

# time = np.arange(0.0,1.0,0.01)
# sin = np.sin(2*np.pi*time)
# cos = np.cos(2*np.pi*time)
#
# test_data = pd.DataFrame(time, columns = ['time'])
# test_data['sin'] = sin
# test_data['cos'] = cos
# test_data.to_csv('data/test.csv', index = False)

tfGen_test = TFGen()
tfGen_test.load_data('./data/test.csv')
# tfGen_test.diff_forward('test1', 'test1_vel')
# tfGen_test.show_current_data()
tfGen_test.write_to_csv('raw_data', 'data/test1.csv')

