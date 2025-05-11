import math
from random import random


# Base is some low-level code (like basic classes and functions)


class Sphere:
    def __init__(self, x, y, r, Vx, Vy):
        self.x = x
        self.y = y
        self.r = r
        self.Vx = Vx
        self.Vy = Vy


def createSpheresList(N, R, V):
    Sprs = []
    for i in range(N):
        good = False
        while not good:
            # Just trying not to get infinite velocity (that breaks code)
            try:
                a = math.pi * random()
                if a < 0.5:
                    Vx = -V / math.sin(a)
                else:
                    Vx = V / math.sin(a)
                b = math.pi * random()
                if b < 0.5:
                    Vy = -V / math.sin(b)
                else:
                    Vy = V / math.sin(b)

                good = True
            except:
                # Pofig
                pass
        """
        # Entropy checking
        Vx = 0
        Vy = 0
        Vx = Vx + 1000
        """
        Sprs.append(Sphere(800 * random(), 600 * random(), R, Vx, Vy))
    return Sprs


def Energy(Sprs: list, m):
    E = 0
    for s in Sprs:
        E = E + m * (s.Vx ** 2 + s.Vy ** 2) / 2
    return E


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
