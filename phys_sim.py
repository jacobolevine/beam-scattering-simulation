import math
import matplotlib.pyplot as plt
import numpy as np

def simulate(y, vx, L, a, k=1, m=1, dt = 0.005):
    vy = 0
    x = -L
    xpos = [x]
    ypos = [y]
    eps = 0.05
    steps = 0
    while abs(x) <= L and steps <= 10000:
        r = math.sqrt(x ** 2 + y ** 2 + eps ** 2)
        force = k * math.exp(-r / a) * ((1 / (r ** 2)) + (1 / (a * r)))
        ax = force * (x / r) / m
        ay = force * (y / r) / m
        vx = vx + ax * dt
        vy = vy + ay * dt
        x = x + vx * dt
        y = y + vy * dt
        xpos.append(x)
        ypos.append(y)
        steps += 1
    theta = math.atan2(vy, vx)
    return theta, xpos, ypos

def run(y0_list, vx0, L, a):
    result = {}
    for i in range(len(y0_list)):
        theta, xpos, ypos = simulate(y0_list[i], vx0, L, a)
        result[(y0_list[i], vx0, a)] = {par: res for par, res in [('theta', theta), ('xpos', xpos), ('ypos', ypos)]}
    return result

if __name__ == '__main__':
    L = 10
    choose_L = input('Choose starting distance from origin? Y/N ')
    if choose_L in ['y', 'Y']:
        L = abs(float(input('Starting distance from origin: ')))
    
    y0_list = np.random.normal(loc=0, scale=1, size=200)
    y0_list = np.clip(y0_list, -5, 5)
    vx0 = 5
    a_list = [0.5, 2, 5]
    theta_means = []

    for a in a_list:
        result = run(y0_list, vx0, L, a)
        theta_list = []
        detector_y_list = []

        plt.figure()

        all_data = list(result.values())
        subset = set(np.random.choice(len(all_data), size=30, replace=False))

        for idx, data in enumerate(all_data):
            xpos = np.array(data['xpos'])
            ypos = np.array(data['ypos'])

            if idx in subset:
                plt.plot(xpos, ypos, linewidth=0.8, alpha=0.6)

            theta_list.append(data['theta'])

            if xpos[-1] >= L:
                detector_y_list.append(ypos[-1])

        plt.axvline(x=L, color='red', linestyle='--')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Random Sample (n=30) Particle Scattering (a={a})')
        plt.ylim(-20, 20)
        plt.axhline(0)
        plt.axvline(0)
        plt.show()

        plt.figure()
        thetas = np.array(theta_list)
        theta_means.append(np.mean(np.abs(thetas)))
        plt.hist(thetas, bins=30)
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title(f'Theta Histogram (a={a})')
        plt.show()

        plt.figure()
        detector_y = np.array(detector_y_list)
        plt.hist(detector_y, bins=30)
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title(f'y at Detection Histogram (a={a})')
        plt.show()

    plt.figure()
    plt.plot(np.array(a_list), np.array(theta_means))
    plt.xlabel('a')
    plt.ylabel('Mean |theta|')
    plt.title('Mean Absolute Scattering Angle vs. Range Parameter')
    plt.axhline(0)
    plt.axvline(0)
    plt.show()
