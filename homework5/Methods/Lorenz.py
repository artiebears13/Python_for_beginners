from scipy.integrate import ode


def lorenz_system(t, xyz):
    th = 10
    r = 28
    b = 8 / 3

    x, y, z = xyz
    dx = th * (y - x)
    dy = x * (r - z) - y
    dz = x * y - b * z
    return [dx, dy, dz]


def lorenz_attractor(xyz0, step):
    t0 = 0
    r = ode(lorenz_system, step)
    r.set_integrator('dopri5')
    r.set_initial_value(xyz0, t0)

    while r.successful():
        r.integrate(r.t + step)
        yield r.y
