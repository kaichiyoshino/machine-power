#%%
import numpy as np
import matplotlib.pylab as plt

#I1, I2
def f1(x, Io, k1, I):
  return Io * (np.exp(k1 * x)- 1) - I

def f2(x, Io, k2, I):
  return Io * (np.exp(k2 * x)- 1) - I

def df1(x, Io, k1):
  return k1 * Io * np.exp(k1 * x)

def df2(x, Io, k2):
  return k2 * Io * np.exp(k2 * x)


#parameter 
v1=1
v2=2
V=0.6
I=0
k1=
k2=

#許容誤差
epsilon1=0.00001



while abs(V - v1 - v2) > epsilon1:
    while True:
        v1 = v1 - f1(v1, 3, 3, I)/df1(v1, 3, 3)
        if abs(f1(v1, 3, 3, I)) < epsilon1:
            break

    while True:
        v2 = v2 - f2(v2, 3, 3, I)/df2(v2, 3, 3)
        if abs(f2(v2, 3, 3, I)) < epsilon1:
            break
    
    I += 0.0001
    print(v1, v2)
            
print(I)
# print(v1, v2)