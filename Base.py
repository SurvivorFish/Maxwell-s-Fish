import math
from random import random, gauss
from parameter import N, k, T, m, w, h, r

molecule_list = [] # Список молекул

class Sphere:
    def __init__(self, x, y, r, Vx, Vy):
        self.x = x
        self.y = y
        self.r = r
        self.Vx = Vx
        self.Vy = Vy


def get_random_coordinates(w: float, h: float):
    x = w*random()
    y = h*random()
    return x,y

def get_random_velocity(T: float, k: float, m: float):
    Vx = gauss(0, math.sqrt(k * T / m))
    Vy = gauss(0, math.sqrt(k * T / m))
    return Vx,Vy

def Energy():
    E = 0
    for s in molecule_list:
        E = E + m * (s.Vx ** 2 + s.Vy ** 2) / 2
    return E

def Temperature():
    return Energy()/N/k

def Entropy():
    nl = 0 # количество молекул слева
    S_T = 0 # Температурная часть энтропии
    for s in molecule_list:
        S_T = S_T + k * math.log(m * (s.Vx ** 2 + s.Vy ** 2) / 2)
        # В какой части находится данная сфера
        if s.x <= w / 2:
            nl = nl + 1

    return k*math.log(math.factorial(N)/math.factorial(nl)/math.factorial(N-nl)) + S_T

# Создание молекул
for i in range(N):
    x, y = get_random_coordinates(w,h)
    Vx, Vy = get_random_velocity(T,k,m)
    molecule = Sphere(x, y, r, Vx, Vy)
    molecule_list.append(molecule)
E_0 = Energy()
S_0 = Entropy()





# Считается столкновение молекул
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
