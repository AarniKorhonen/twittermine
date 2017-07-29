import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x, y =  np.loadtxt('tweets.20170729-064621.csv', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
