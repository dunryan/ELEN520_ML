#1. Write a Python program to calculate the estimated slope and coefficient for the Computer Repair dataset
#  using the expressions derived by the method of least squares. 

import numpy as np


df  = np.array([ 23 ,1 ,29, 2 ,49 ,3 ,64 ,4 ,74 ,4 ,87 ,5 ,96 ,6 ,97 ,6 ,109 ,7 ,119 ,8 ,149 ,9 ,145 ,9 ,154 ,10 ,166 ,10 ])
df = df.reshape(14,2)

len(df[:,1])
xsq = [0]*len(df[:,1])
xy = [0]*len(df[:,1])
for i in range(len(df)):
    xsq[i] = df[i,0]*df[i,0]
    xy[i] = df[i,0]*df[i,1] 
print(xsq)
print(xy)

sum_xsq = sum(xsq)
sum_xy = sum(xy)
sum_x = sum(df[:,0])
sum_y = sum(df[:,1])
N = len(df[:,1])
print(sum_xsq)
print(sum_xy)
print(sum_x)
print(sum_y)

# Compute slope
m = (N*(sum_xy)-sum_x*sum_y)/(N*sum_xsq - sum_x*sum_x)
print(m)

# Compute Y-intercept
b = (sum_y - m*sum_x)/N
print(b)

import matplotlib.pyplot as plt
xTest = np.arange(0,160)
yTest = m*xTest+b

plt.scatter(df[:,0],df[:,1])
plt.plot(xTest,yTest,c='red')
plt.xlabel('Minutes')
plt.ylabel('Units')

# Compute correlation coefficient
yi_diff_ybar = [0]*len(df[:,1])
xi_diff_ybar = [0]*len(df[:,1])
xi_diff_ybarSQ = [0]*len(df[:,1])
yi_diff_ybarSQ = [0]*len(df[:,1])
for i in range(len(df[:,0])):
    yi_diff_ybar[i]= df[i,1] - (sum(df[:,1])/N)
    xi_diff_ybar[i] = df[i,0] - (sum(df[:,0])/N)
    xi_diff_ybarSQ[i] = xi_diff_ybar[i]*xi_diff_ybar[i]
    yi_diff_ybarSQ[i] = yi_diff_ybar[i]*yi_diff_ybar[i]
    
sx = np.sqrt((sum(xi_diff_ybarSQ))/(N-1))
sy = np.sqrt((sum(yi_diff_ybarSQ))/(N-1))

r = 1/(N-1)*(sum(yi_diff_ybar)/sy)*(sum(xi_diff_ybar)/sx)