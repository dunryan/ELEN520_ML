# 3. Define a class called Point2D that has two private attributes __x and __y to represent a 2-D value (x,y).
# Add a constructor __init__() function that takes self, x and y as parameters and assigns them to the private attributes.
# Add accessor methods called getX(self) and getY(self).

class Point2D:
    def __init__(self,x,y):
        self.xValue = x
        self.yValue = y

    def getXValue(self):
        return self.xValue
    
    def getYValue(self):
        return self.yValue