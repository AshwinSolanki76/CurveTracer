import turtle
import numpy as np
from Theme import Themes
from Theme import randomTheme

class Curve:
    def __init__(self,name="Title",windowHeight=800,windowWidth=1600,canvasHeight=7000,canvasWidth=10000) -> None:
        
        # turtle.setup(windowWidth,windowHeight) #make changes in window size 1537 760
        self.window=turtle
        self.window.hideturtle()
        self.canvasWidth=canvasWidth
        self.canvasHeight=canvasHeight

        self.penSpeed=100000

        self.CurvePenStrokeSize=2
        self.AxisPenStrokeSize=1
        self.AxisPenColour=(0,0,0)
        self.CurvePenColour=(0,0,0)
        self.bgColour=(255,255,255)

        self.window.screensize(canvasWidth,canvasHeight) #make changes in canvas
        self.window.getcanvas().master.geometry('{}x{}+{}+{}'.format(windowWidth, windowHeight, -10,0))

        self.window.title(name)

        self.window.Screen().colormode(255)
        self.window.Screen().bgcolor(self.bgColour)
        self.window.pencolor(self.AxisPenColour)
        self.window.pensize(10)
        self.window.speed(10000)
        # __class__.MakeAxis
        # self.window.done()
    
    def applyTheme(self,name):
        '''Sets Pencolour and bg colour'''
        self.bgColour=Themes[name]['bg']
        # self.
        # self.window.pensize(3)
        self.CurvePenStrokeSize=5
        self.setBgColour(Themes[name]['bg'])
        self.setAxisPenColour(Themes[name]['ax'])
        self.setCurvePenColour(Themes[name]['pen'])
    def ApplyRandomTheme(self):
        self.bgColour=randomTheme['bg']
        # self.
        # self.window.pensize(3)
        self.CurvePenStrokeSize=5
        self.setBgColour(randomTheme['bg'])
        self.setAxisPenColour(randomTheme['ax'])
        self.setCurvePenColour(randomTheme['pen'])


    def setWindowName(self,name):
        self.window.title(name)

    def setAxisPenSize(self,size):
        self.AxisPenStrokeSize=size
        self.window.pensize(size)
    def setCurvePenSize(self,size):
        self.CurvePenStrokeSize=size
        self.window.pensize(size)
    def setPenSpeed(self,speed):
        self.penSpeed=speed
        self.window.speed(speed)
    def setAxisPenColour(self,colour):
        self.AxisPenColour=colour
        self.window.pencolor(colour)
    def setCurvePenColour(self,colour):
        self.CurvePenColour=colour
        self.window.pencolor(colour)


    def setBgColour(self,colour):
        self.bgColour=colour
        self.window.Screen().bgcolor(colour)
    
    def ColourSetter():
        '''Change Background Colour and Pen(stroke) Colour'''
        pass

    def MakeAxis(self):
        self.window.up()
        self.setAxisPenColour(self.AxisPenColour) #15,52,96
        # self.window.pensize(1)
        self.setAxisPenSize(self.AxisPenStrokeSize)
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
        # self.window.pensize(5)
        self.setCurvePenSize(self.CurvePenStrokeSize)
        self.setCurvePenColour(self.CurvePenColour)
        for i in zip(x,y):
            self.window.goto(i)
        print("Done")


def x(x):
    return (x**3)/10000

c=Curve()
c.setWindowName("Apple")
# c.applyTheme('DarkAndYello')
# c.applyTheme()
c.ApplyRandomTheme()
c.MakeAxis()

c.trace(x,start=-150,stop=150,step=500)
c.window.done()
