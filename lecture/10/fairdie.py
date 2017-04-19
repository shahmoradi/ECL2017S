import numpy as np

def throwFairDie():
    import random as rnd
    return rnd.randint(1, 6)

def getMeanDieValue(n=100):
    meanDieValue = np.zeros((n,6),dtype=np.double)
    randomThrow = throwFairDie() - 1        # assign the first value to the above array
    meanDieValue[0,randomThrow] = 1.0 / 1.0 # one try so far, one success for the die value that is obtained.
    for i in range(1,n):
        randomThrow = throwFairDie() - 1
        meanDieValue[i,randomThrow] = 1.0   # add one success for the value obtained
        meanDieValue[i,:] += meanDieValue[i-1,:]    # combine the recent success with the total number of successes from previous tries.
        meanDieValue[i-1,:] /= np.double(i+1)  # Now normalize the values form the last try to the total number of tries.
    meanDieValue[-1:,:] /= np.double(n)  # Now normalize the very last try to the total number of tries.
    return meanDieValue

print(getMeanDieValue()[-1:,:])