import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from animation import animirien, fig
from parameter import dt, doDraw


if __name__ == '__main__':
    ani = FuncAnimation(fig, animirien, interval=dt)
    plt.show()
