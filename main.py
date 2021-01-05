from os import spawnl
import turtle
import numpy as np

class Curve:
    def __init__(self,name="Title",windowHeight=800,windowWidth=1600,canvasHeight=7000,canvasWidth=10000) -> None:
        
        # turtle.setup(windowWidth,windowHeight) #make changes in window size 1537 760
        self.window=turtle
        self.canvasWidth=canvasWidth
        self.canvasHeight=canvasHeight
        self.window.screensize(canvasWidth,canvasHeight) #make changes in canvas
        self.window.getcanvas().master.geometry('{}x{}+{}+{}'.format(windowWidth, windowHeight, -10,0))

        self.window.title(name)

        self.window.Screen().colormode(255)
        self.window.Screen().bgcolor(26,26,46)
        self.window.pencolor(233,69,96)
        self.window.pensize(10)
        self.window.speed(10000)
        # __class__.MakeAxis
        # self.window.done()

    def setWindowName(self,name):
        self.window.title(name)
    def setPenSize(self,size):
        self.window.pensize(size)
    def setPenSpeed(self,speed):
        self.window.speed(speed)
    def getPenColour(self):
        pass
    def ColourSetter():
        '''Change Background Colour and Pen(stroke) Colour'''
        pass

    def MakeAxis(self):
        self.window.up()
        self.window.pencolor(15,52,96)
        self.window.pensize(1)
        self.window.goto(-1000,0)
        self.window.down()
        self.window.goto(1000,0)
        self.window.up()
        self.window.goto(0,0)
        self.window.down()
        self.window.goto(0,1000)
        self.window.goto(0,-1000)
        self.window.goto(0,0)

    def trace(self,func,start=0,stop=1000,step=1000):
        x=np.linspace(start,stop,step)
        self.window.pensize(2)
        self.window.pencolor(233,69,96)
        y=list(map(func,x))
        self.window.up()
        self.window.goto(x[0],y[0])
        self.window.down()
        for i in zip(x,y):
            self.window.goto(i)
        print("Done")


def x(x):
    return (x**3)/10000

c=Curve()
c.MakeAxis()
c.setWindowName("Apple")
c.trace(x,start=-500,stop=500,step=1000)
c.window.done()


# turtle.up()
# turtle.goto(0,0)
# turtle.down()
# turtle.goto(100,500)
# turtle.done()