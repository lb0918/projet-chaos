from math import pi, cos, sin
import numpy as np
import matplotlib.colors as mcolors
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

x_ = np.linspace(0, 314, 50)
y_ = np.linspace(0, 314, 50)
X, Y = np.meshgrid(x_, y_)

t_ = np.linspace(0, 2*pi, 90)



def f(x, y):
  return np.sin(x/50) * np.cos(y/50) * 50 + 50

def g(x, y, t):
  return f(x*cos(t) - y*sin(t), x*sin(t) + y*cos(t))

fig = plt.figure()
ax = fig.add_subplot(projection = "3d")

def animate(n):
    ax.cla()
    Z = g(X, Y, t_[n])
    colorfunction = (X**2+Y**2+Z**2)
    norm = mcolors.Normalize(colorfunction.min(), colorfunction.max())
    ax.plot_surface(
      X, Y, Z, rstride = 1, cstride = 1, facecolors=cm.jet(norm(colorfunction))
    )
    ax.set_zlim(0, 100)
    return fig


anim = FuncAnimation(
  fig = fig, func = animate, frames = len(t_), interval = 1, repeat = False
)

writergif = PillowWriter(fps=30)
anim.save('filename22.gif',writer=writergif)

