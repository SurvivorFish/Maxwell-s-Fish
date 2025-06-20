import math
import random

from Base import Sphere
from parameter import w, h, N, dt, alpha, m, k, T

# Sarcophilus harrisii
type_of_Dmitriy = 3  # Тип демона


def dimon(s: Sphere, Demons_Entropy: float):
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
            return dimon_1(s, ddt2, Demons_Entropy)
        if type_of_Dmitriy == 2:
            return dimon_2(s, ddt2, Demons_Entropy)
        if type_of_Dmitriy == 3:
            return dimon_3(s, ddt2, Demons_Entropy)

    # Если молекула не может столкнуться с демоном, то пусть летит себе дальше
    return True, Demons_Entropy  # Показывает, что молекула не взаимодействовала с демоном и может двигаться (время dt не было учтено)


# По модулям
def dimon_1(s: Sphere, ddt2: float, Demons_Entropy: float):
    # Проверка: если молекула летит вправо и имеет большую скорость, то отражается и наоборот тоже
    if s.Vx * (m * (s.Vx ** 2 + s.Vy ** 2) - k * T) > 0:
        s.Vx = -s.Vx
    else:
        # Если молекула не отражается, значит она взаимодействует с демоном. То есть он должен что-то записать про неё в свою информацию
        Demons_Entropy = Demons_Entropy + math.log2(N)
    s.x = s.x + s.Vx * ddt2
    s.y = s.y + s.Vy * ddt2
    return False, Demons_Entropy


# По углам
def dimon_2(s: Sphere, ddt2: float, Demons_Entropy: float):
    if s.Vx > 0:
        s.Vx = -s.Vx
    if (s.Vx < 0 and s.Vy < 0 and abs(s.Vx) > abs(s.Vy)) or (
            s.Vx > 0 and s.Vy > 0 and abs(s.Vx) < abs(s.Vy)):
        s.Vx, s.Vy = s.Vy, s.Vx
    if (s.Vx < 0 and s.Vy > 0 and abs(s.Vx) > abs(s.Vy)) or (
            s.Vx > 0 and s.Vy < 0 and abs(s.Vx) < abs(s.Vy)):
        s.Vx, s.Vy = -s.Vy, -s.Vx
    else:
        s.Vx = -s.Vx
    s.x = s.x + s.Vx * ddt2
    s.y = s.y + s.Vy * ddt2
    return False, Demons_Entropy


def dimon_3(s: Sphere, ddt2: float, Demons_Entropy: float):
    # Вообще, трудно представить, что это...
    # Будем думать, как Шендерович (вспомню лекции)
    # Просто есть какая-то энергия, которая тратится на проход через демона. Но есть какая-то вероятность, что демон не сработает в обратном направлении (пропустит молекулы)
    # Эта вероятность - по Гиббсу
    # Энергия, необходимая для прохода через демона
    E = k * T / 2
    # Переменная, означающая, открылась ли дверь случайно
    door_opened = (math.exp(-E / k / T) >= random.random())
    # Если дверь не открыта случайно, значит демон работает. В противном случае молекула просто пролетает
    if not door_opened:
        # Если летела справа, то сталкивается с демоном и отдаёт часть энергии на проход
        E_0 = m * (s.Vx ** 2 + s.Vy ** 2) / 2
        if s.Vx < 0 and E_0 > E:
            s.Vx = s.Vx * math.sqrt(1 - E / E_0)
            s.Vy = s.Vy * math.sqrt(1 - E / E_0)
            Demons_Entropy = Demons_Entropy + 2 * E / T
        # Если летела слева, то отражаем
        else:
            s.Vx = -s.Vx
            # Ничего на это не тратится, потому энтропию не меняем
    s.x = s.x + s.Vx * ddt2
    s.y = s.y + s.Vy * ddt2
    return False, Demons_Entropy
