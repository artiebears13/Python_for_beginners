from Lorenz import lorenz_attractor
import matplotlib.pyplot as plt

TimeMod = 30.
t0 = 0.
x0 = 0.
y0 = 1.
z0 = 1.05
xyz0 = (x0, y0, z0)
step = 0.1
l1 = lorenz_attractor([1, 2, 3], step)
l2 = lorenz_attractor([2, 3, 4], step)

fig = plt.figure('Lorenz')
ax = plt.axes(projection='3d')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_zlim(0, 30)

sx1,sy1, sz1, sx2, sy2, sz2 = [0], [0], [0], [0], [0],[0]

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

plt.plot(sx1, sy1, sz1)
plt.plot(sx2, sy2, sz2)
plt.draw()
plt.show()
