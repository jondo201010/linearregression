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

    def getAverageDistance(self,dataFram):
        dataFram[2]=getDistance(dataFram[0],dataFram[1]);
        return dataFram[2].


#  git config --global user.email "jondo201010@gmail.com"