import math

from Base import Sphere
from parameter import w, h, dt, alpha, m, k, T

# Sarcophilus harrisii

type_of_Dmitriy = 1  # Тип демона


def dimon(s: Sphere):
    # Молекула может столкнуться с демоном?
    if (s.x <= w / 2 <= s.x + s.Vx * dt / alpha) or (s.x >= w / 2 >= s.x + s.Vx * dt / alpha):
        ddt1 = (w / 2 - s.x) / s.Vx  # Время, необходимое молекуле, чтоб долететь до демона

        # Молекула пролетает нужное растояние
        s.x = w / 2
        s.y = s.y + s.Vy * ddt1

        # Оставшееся время
        ddt2 = dt / alpha - ddt1

        # Вызываем нужную модель демона
        if type_of_Dmitriy == 1:
            return dimon_1(s, ddt2)
        if type_of_Dmitriy == 2:
            return dimon_2(s, ddt2)

    # Если молекула не может столкнуться с демоном, то пусть летит себе дальше
    return True  # Показывает, что молекула не взаимодействовала с демоном и может двигаться (время dt не было учтено)


# По модулям
def dimon_1(s: Sphere, ddt2: float):
    # Проверка: если молекула летит вправо и имеет большую скорость, то отражается и наоборот тоже
    if s.Vx * (m*(s.Vx ** 2 + s.Vy ** 2) - k * T) > 0:
        s.Vx = -s.Vx
    s.x = s.x + s.Vx * ddt2
    return False


# По углам
def dimon_2(s: Sphere, ddt2: float):
    if s.Vx > 0:
        s.Vx = -s.Vx
    '''if (s.Vx < 0 and s.Vy < 0 and abs(s.Vx) > abs(s.Vy)) or (
            s.Vx > 0 and s.Vy > 0 and abs(s.Vx) < abs(s.Vy)):
        s.Vx, s.Vy = s.Vy, s.Vx
    if (s.Vx < 0 and s.Vy > 0 and abs(s.Vx) > abs(s.Vy)) or (
            s.Vx > 0 and s.Vy < 0 and abs(s.Vx) < abs(s.Vy)):
        s.Vx, s.Vy = -s.Vy, -s.Vx
    else:
        s.Vx = -s.Vx'''
    s.x = s.x + s.Vx * ddt2
    s.y = s.y + s.Vy * ddt2
    return False
