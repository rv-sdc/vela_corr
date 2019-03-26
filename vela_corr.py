import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from math import*
from scipy.fftpack import fft

#load file
array= np.loadtxt('/home/akshatha/SWAN/ch00_B0833-45_20150612_191438_010_4')
north=array[:,0]
south=array[:,1]

#create empty array for stacking
array2d=[]
array_new=[]

#averaging 512 point spectrum for 200 times and stacking them in array2dx

for j in range(1,301):
	for i in range(1,201):
	   ffty=fft(north[(i-1)*512: i*512-1])	#fft of 512 points
	   half=ffty[256:511]                   #take second half, fft follows hermitian symmetry
	   realpart1= np.square(half.real)
	   imagpart1=np.square(half.imag)
	   amp1=np.sqrt(realpart1+ imagpart1)   #amplitude
	   array2d.append(amp1)           

	array2dx=np.vstack(array2d)             #stack 200 spectrums
	array2d_mean=array2dx.mean(0)           #calculate columnwise mean
	array_new.append(array2d_mean)         
img=np.vstack(array_new)                        #stack the averaged spectrum
med=np.median(img,axis=0)                       #calculate median
img_new=np.subtract(img,med)	                #remove median noise


#Plot FFT of North
plt.plot(img[:,1])
plt.show()
plt.plot(array2dx[0:256,0])
plt.show()
plt.imshow(img_new)
plt.xlabel('Frequency Channels')
plt.ylabel('512/33 us each')
plt.title('North Array data')
#plt.savefig('vela_north.png')
plt.show()





