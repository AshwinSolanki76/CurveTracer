from main import Curve
import numpy as np

c=Curve("Apple")
def x(x):
    return 100*np.sin(x/100)
c.ApplyRandomTheme()
c.trace(x,start=-500,stop=500,step=500)
c.window.done()