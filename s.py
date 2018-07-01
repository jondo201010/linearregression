import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import math
from Line import Line



def LoadDataPoints():
    return pd.read_csv("linear_regression_data.txt", names=['Population','Profit'],header=None);



def GetInitialGuessLine(fullData):

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
    plt.plot([initialGuessLine_Point1_x, initialGuessLine_Point2_x], [initialGuessLine_Point1_y, initialGuessLine_Point2_y], 'k-', lw=2)
    ln= Line(initialGuessLine_Point1_x,initialGuessLine_Point1_y,initialGuessLine_Point2_x,initialGuessLine_Point2_y)
    return ln


fullData = LoadDataPoints()
currentGuessLine=GetInitialGuessLine(fullData)
print(currentGuessLine.getDistance(10,13))
plt.show()


