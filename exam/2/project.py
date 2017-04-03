import scipy.io
import matplotlib.pyplot as plt
import numpy as np

mat = scipy.io.loadmat('cells.mat')
cells = mat['cells']
testSlice = cells[:,:,9,3]

#fig, (ax1) = plt.subplots(nrows=3, ncols=3, figsize=(10,10))
fig, (ax1) = plt.subplots(figsize=(10,10))

ax1.imshow(testSlice, aspect=6/4) #, extent=[0,100,0,1], aspect=100)
ax1.set_title('Tumor slice')

plt.tight_layout()
plt.show()

