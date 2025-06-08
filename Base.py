import math
import tkinter
import tkinter as tk
import random

# Просто какие-то базовые классы, функции и константы

fps = 30  # frames per second. Physics time resolution is also fps
dt = 1 / fps
w = 800  # Высота окна (и сосуда)
h = 600  # Ширина окна (и сосуда)
k = 1.38 * 10 ** -16  # Bolcman's postoyannaya
m = 6.65 * 10 ** -24  # mass of molecule of He
# Как и ожидалось, при высоких температурах молекулы емаё как летают
T = 0.001

# Настройка TKinter
lin = tk.Tk()  # Setting up tkinter
lin.title("Our Super Program 1")
lin.geometry(f'{w}x{h}')
canvas = tkinter.Canvas(lin)
canvas.configure(bg="white")
canvas.pack(fill="both", expand=True)

class Sphere:
    def __init__(self, x, y, r, Vx, Vy, ts):
        self.x = x
        self.y = y
        self.r = r
        self.Vx = Vx
        self.Vy = Vy
        self.ts = ts  # объект сферы в TKinter


def createSpheresList(N, R, V):
    Sprs = []
    # Создание сферы
    for i in range(N):
        Vx = random.gauss(0, math.sqrt(k*T/m))
        Vy = random.gauss(0, math.sqrt(k*T/m))
        # Расположение в сосуде
        good = False
        while not good:
            x = R + (w - 2 * R) * random.random()
            y = R + (h - 2 * R) * random.random()
            if len(canvas.find_overlapping(x - R, y - R, x + R, y + R)) == 0:
                good = True

        stupidity = canvas.create_oval(x - R, y - R, x + R, y + R, fill="blue", outline="Black", width=1)
        Sprs.append(Sphere(x, y, R, Vx, Vy, stupidity))
    return Sprs


def Energy(Sprs: list, m: float):
    E = 0
    for s in Sprs:
        E = E + m * (s.Vx ** 2 + s.Vy ** 2) / 2
    return E


def Entropy(Sprs: list, m: float):
    N = len(Sprs)
    nl = 0 # количество молекул слева
    S_T = 0 # Температурная часть энтропии
    for s in Sprs:
        S_T = S_T + k * math.log(m * (s.Vx ** 2 + s.Vy ** 2) / 2)
        # В какой части находится данная сфера
        if s.x <= w / 2:
            nl = nl + 1

    return k*math.log(math.factorial(N)/math.factorial(nl)/math.factorial(N-nl)) + S_T


# Calculating bubuh
def bubuh(Vx1, Vy1, Vx2, Vy2, rx, ry):
    theta = math.atan2(ry, rx)
    Va1 = Vx1 * math.cos(theta) + Vy1 * math.sin(theta)
    Vb1 = - Vx1 * math.sin(theta) + Vy1 * math.cos(theta)
    Va2 = Vx2 * math.cos(theta) + Vy2 * math.sin(theta)
    Vb2 = - Vx2 * math.sin(theta) + Vy2 * math.cos(theta)

    Va1, Va2 = Va2, Va1

    Vx1f = Va1 * math.cos(theta) - Vb1 * math.sin(theta)
    Vy1f = Va1 * math.sin(theta) + Vb1 * math.cos(theta)
    Vx2f = Va2 * math.cos(theta) - Vb2 * math.sin(theta)
    Vy2f = Va2 * math.sin(theta) + Vb2 * math.cos(theta)
    return Vx1f, Vy1f, Vx2f, Vy2f
