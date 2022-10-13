from Lorenz import lorenz_attractor
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

def init():
    line.set_data([], [])
    return line,


# animation function of dataframes' list
def animate_xy(i):
    line.set_data(sx1[:i], sy1[:i])

    # p = sns.lineplot(x=sx1, y=sy1,  color="r")

    # plt.setp(p.lines, linewidth=1)
    return line,

def animate_xz(i):
    line.set_data(sx1[:i], sz1[:i])

    # p = sns.lineplot(x=sx1, y=sy1,  color="r")

    # plt.setp(p.lines, linewidth=1)
    return line,


TimeMod = 30.
t0 = 0.
x0 = 0.
y0 = 1.
z0 = 1.05
xyz0 = (x0, y0, z0)
step = 0.1
l1 = lorenz_attractor([1, 2, 3], step)
l2 = lorenz_attractor([2, 3, 4], step)
'''
fig = plt.figure('Lorenz')
ax = plt.axes(projection='3d')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_zlim(0, 30)
'''

sx1, sy1, sz1, sx2, sy2, sz2 = [0], [0], [0], [0], [0], [0]

Time = 0.0

for p1, p2 in zip(l1, l2):

    print(p1, p2)
    sx1.append(p1[0])
    sy1.append(p1[1])
    sz1.append(p1[2])
    sx2.append(p2[0])
    sy2.append(p2[1])
    sz2.append(p2[2])

    Time += step
    if Time >= TimeMod:
        break

# plt.plot(sx1, sy1, sz1)
# plt.plot(sx2, sy2, sz2)
# plt.draw()
# plt.show()
'''
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(sx1, sy1)
ax[0, 0].plot(sx2, sy2)
ax[0, 0].set_title('x,y')

ax[0, 1].plot(sx1, sz1)
ax[0, 1].plot(sx2, sz2)
ax[0, 1].set_title('x,z')

ax[1, 0].plot(sy1, sz1)
ax[1, 0].plot(sy2, sz2)
ax[1, 0].set_title('y,z')

ax = fig.add_subplot(2, 2, 3, projection='3d')


ax.plot(sx1, sy1, sz1)
ax.plot(sx1, sy1, sz1)
ax.set_title('x,y,z')
'''

fig = plt.figure(figsize=(10, 10))
fig.suptitle('Lorenz Attractor')
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(sx1, sy1)
ax1.plot(sx2, sy2)
ax1.set_title('x,y')
ax1.grid()
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(sx1, sz1)
ax2.plot(sx2, sz2)
ax2.set_title('x,z')
ax2.grid()
ax2.set_xlabel('x')
ax2.set_ylabel('z')

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(sy1, sz1)
ax3.plot(sy2, sz2)
ax3.set_title('y,z')
ax3.grid()
ax3.set_xlabel('y')
ax3.set_ylabel('z')

ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.plot(sy1, sz1, sz1)
ax4.plot(sy2, sz2, sz2)
ax4.set_title('x,y,z')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('z')

# plt.show()
print(len(sx1))

fig = plt.figure()
ax = plt.axes(xlim=(-30, 30), ylim=(-30, 30))



line, = ax.plot([], [], lw=2)
anim = animation.FuncAnimation(fig, animate_xy,
                               frames=len(sx1), interval=10, blit=False)

plt.show()
