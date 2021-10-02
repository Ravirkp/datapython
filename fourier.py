from scipy.fftpack import fft 
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, np.pi*10, 0.05)
y = np.sin(x)
p = np.cos(x)
plt.plot(x,p)
plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.show()