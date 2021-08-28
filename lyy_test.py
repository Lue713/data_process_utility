from tf_gen import TFGen

tfGen = TFGen()
tfGen.load_data('./data/test.csv')
tfGen.diff_forward('test1', 'test1_vel')
tfGen.show_current_data()