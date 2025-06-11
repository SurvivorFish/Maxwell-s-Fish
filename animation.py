import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from physik import tritt, lage
from parameter import karton_lange, karton_breite, N

fig, ax = plt.subplots()
sc = ax.scatter(lage[:,0], lage[:,1], s=10)
ax.set_xlim(0, karton_lange)
ax.set_ylim(0, karton_breite)
ax.axvline(karton_lange/2, color='green', linestyle='solid')

def animirien(frame):
    tritt()
    sc.set_offsets(lage)
    return sc

def run():
    ani = FuncAnimation(fig, animirien, frames=300, interval=50)
    plt.show()

