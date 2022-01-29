import numpy as np
import matplotlib.pyplot as plt
# Preprocessing Input data
X = np.array(eval(input()))
Y = np.array(eval(input()))
# Building the model
XMean=np.mean(X)
YMean=np.mean(Y)
num,den=0,0
for i in range(len(X)):
  num+=(X[i]-XMean)*(Y[i]-YMean)
  den+=(X[i]-XMean)**2
m=num/den
#y=mx+c
c=YMean-m*XMean
print (m, c)
#Predict the output
Y_pred=m*X+c
print (Y_pred)
#Plotting the graph
plt.scatter(X,Y)
plt.plot(X,Y_pred,color="red")
plt.show()