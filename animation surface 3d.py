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

x = np.linspace(1,100,50)
y = np.linspace(1,100,50)
t = np.linspace(1,5,100)
X1, Y1 = np.meshgrid(x,y)


a = 10
sigma = 1
def u(x,y,t):
    alpha = 90-np.arctan(y/x)
    b = 3
    omega = (3*(a**2)*(b**2)-a**4)/(4*a)
    res = 0.5*(a**2)*(1/np.cosh(0.5*a*(x-b*y-(omega*t/a))))**2
    return res


def f(x, y):
  return np.sin(x/50) * np.cos(y/50) * 50 + 50

def g(x, y, t):
  return f(x*cos(t) - y*sin(t), x*sin(t) + y*cos(t))

fig = plt.figure()
ax = fig.add_subplot(projection = "3d")

# def animate(n):
#     ax.cla()
#     Z = g(X, Y, t_[n])
#     colorfunction = (X**2+Y**2+Z**2)
#     norm = mcolors.Normalize(colorfunction.min(), colorfunction.max())
#     ax.plot_surface(
#       X, Y, Z, rstride = 1, cstride = 1, facecolors=cm.jet(norm(colorfunction))
#     )
#     ax.set_zlim(0, 100)
#     return fig

def animate1(n):
    ax.cla()
    Z = u(X1, Y1, t[n])
    colorfunction = (X1**2+Y1**2+Z**2)
    norm = mcolors.Normalize(colorfunction.min(), colorfunction.max())
    ax.plot_surface(
      X1, Y1, Z, rstride = 1, cstride = 1, facecolors=cm.jet(norm(colorfunction))
    )
    ax.set_zlim(0, 50)
    return fig


anim1 = FuncAnimation(
  fig = fig, func = animate1, frames = len(t), interval = 1, repeat = True
)

writergif = PillowWriter(fps=30)
anim1.save('test.gif',writer=writergif)



# anim = FuncAnimation(
#   fig = fig, func = animate, frames = len(t_), interval = 1, repeat = False
# )

# writergif = PillowWriter(fps=30)
# anim.save('filename232432.gif',writer=writergif)

