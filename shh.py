import numpy as np
import matplotlib.pyplot as plt

# параметры
N = 100
karton_lange = 10
karton_breite = 5
dt = 0.01
grenze_v = 100

# начальные координаты и скорости
lage = np.random.rand(N, 2) * [karton_lange, karton_breite]
gwekit = np.random.randn(N, 2) * 20

# функция обновления
def tritt():
    global lage, gwekit
    for i in range(N):
        x, y = lage[i]
        vx, vy = gwekit[i]

        # отражения от границ
        if x <= 0 or x >= karton_lange:
            gwekit[i, 0] *= -1
        if y <= 0 or y >= karton_breite:
            gwekit[i, 1] *= -1
        if abs(x - karton_lange / 2) < 0.05:
            v = np.linalg.norm(gwekit[i])
            if x < karton_lange / 2 and vx > 0 and v > grenze_v:
                gwekit[i, 0] *= -1
            elif x > karton_lange / 2 and vx < 0 and v < grenze_v:
                gwekit[i, 0] *= -1
        lage[i] += gwekit[i] * dt

# отрисовка
plt.ion()
fig, ax = plt.subplots()
sc = ax.scatter(lage[:, 0], lage[:, 1], s=10)
ax.set_xlim(0, karton_lange)
ax.set_ylim(0, karton_breite)
ax.axvline(karton_lange / 2, color='green', linestyle='-')

# анимация вручную
for frame in range(1000):
    tritt()
    sc.set_offsets(lage)
    plt.pause(0.01)

plt.ioff()
plt.show()
