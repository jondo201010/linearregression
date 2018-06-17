import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import math


class Line:
    def __init__(self, x1,y1,x2,y2):
        self.slope=(y2-y1)/(x2-x1)
        self.y_intercept=y2-self.slope*x2

    def getSlope(self):
        return self.slope

    def getIntercept(self):
        return self.y_intercept

    def getDistance(self,x,y):
        dist=abs(self.y_intercept+self.slope*x-y)/(math.sqrt(1+self.slope**2))
        return dist



fullData=pd.read_csv("linear_regression_data.txt", names=['Population','Profit'],header=None)

#plt.plot(x=fullData['Population'], y=fullData['Profit'])

plt.scatter(fullData['Population'],  fullData['Profit'])
#plt.plot([10, 20], [5, 20], 'k-', lw=2)
x=fullData['Population']
y=fullData['Profit']


# To start get Two Points
# First Point
# average of x and y
initialGuessLine_Point1_x=x.mean()

initialGuessLine_Point1_y =y.mean()


# point 2
# Max(x)-Min(x),Max(y)-Min(y)
initialGuessLine_Point2_x=(x.max()+x.min())/2

initialGuessLine_Point2_y =(y.max()+y.min())/2
print(initialGuessLine_Point1_x,initialGuessLine_Point1_y)
print(initialGuessLine_Point2_x,initialGuessLine_Point2_y)
print(x.max(),x.min())
plt.plot([initialGuessLine_Point1_x, initialGuessLine_Point2_x], [initialGuessLine_Point1_y, initialGuessLine_Point2_y], 'k-', lw=2)

ln= Line(initialGuessLine_Point1_x,initialGuessLine_Point1_y,initialGuessLine_Point2_x,initialGuessLine_Point2_y)
print(ln.getDistance(10,13))
plt.show()


