import numpy as np
array= np.loadtxt('/home/rajan/SWAN/Vela_Data-20190326T015923Z-001/Vela_Data/ch00_B0833-45_20150612_191438_010_4')
np.save('datafile',array)
print('done')