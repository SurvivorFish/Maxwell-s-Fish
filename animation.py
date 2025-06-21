import time

import matplotlib.pyplot as plt
from parameter import w, h, r, dt, alpha, doGraph, doPrint, VanDerGulinyan
from Base import molecule_list, Energy, Entropy, Temperature, E_0, S_0, bubuh
from Maxwell_demon import dimon
import keyboard

if doGraph:
    time0 = time.time()
    # Массивы для графиков
    GraphTime = [] # Массив времён
    Et = [] # Массив энергий всего сосуда
    St = [] # Массив энтропий всего сосуда
    Tt = [] # Массив температур всего сосуда
    Tdt = [] # Массив температуры демона
    Nl = [] # Массив количества молекул слева
    Nr = [] # Массив количества молекул справа
    MegaFile = open('Graph data/Data.txt', 'w')

# Характеристики Демона
Demons_Entropy = 0
Demons_Temperature = 250

xs = []  # Список x-овых координат молекул
ys = []  # Список y-овых координат молекул
coords = []  # Список координат [x,y]
for molecule in molecule_list:
    x = molecule.x
    y = molecule.y
    xs.append(x)
    ys.append(y)
    coords.append([x, y])


# функция обновления
def tritt():
    global Demons_Entropy
    global Demons_Temperature
    coords.clear()
    xs.clear()
    ys.clear()
    nl = 0
    nr = 0

    # Цикл, обрабатывающий физику для каждой молекулы
    for molecule in molecule_list:
        # отражения от границ
        if molecule.x <= r or molecule.x >= w - r:
            molecule.Vx = -molecule.Vx
        if molecule.y <= r or molecule.y >= h - r:
            molecule.Vy = -molecule.Vy

        can_move, Demons_Entropy, Demons_Temperature = dimon(molecule, Demons_Entropy, Demons_Temperature)

        if VanDerGulinyan and can_move:
            for other in molecule_list:
                if (other.x - molecule.x)**2 + (other.y - molecule.y)**2 < r**2:
                    bubuh(molecule, other)
        if can_move:
            # Обновление координат молекул
            molecule.x = molecule.x + molecule.Vx * dt / alpha
            molecule.y = molecule.y + molecule.Vy * dt / alpha

        if doGraph:
            if molecule.x < w/2:
                nl = nl + 1
            else:
                nr = nr + 1

        # Обновление списков для MathPlotLib
        x = molecule.x
        y = molecule.y
        xs.append(x)
        ys.append(y)
        coords.append([x, y])

        if doPrint:  # Пишу энергию, энтропию
            print(Entropy() - S_0, Entropy() - S_0 + Demons_Entropy)
    if doGraph:
        GraphTime.append(time.time() - time0)
        Et.append(Energy())
        St.append(Entropy() - S_0 + Demons_Entropy)
        Tt.append(Temperature())
        Tdt.append(Demons_Temperature)
        Nl.append(nl)
        Nr.append(nr)


# ==============================
# Рисование
# ==============================
# Создание списков координат для работы MathPlotLib


fig = plt.figure()
ax = plt.subplot()
sc = ax.scatter(xs, ys, s=10)


# функция анимации
def animirien(frame):
    tritt()
    ax.clear()
    sc = ax.scatter(xs, ys, s=10)
    sc.set_offsets(coords)

    # Создание осей
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    # Рисование полосочки, означающей демона
    ax.axvline(w / 2, color='green', linestyle='solid')
    if keyboard.is_pressed('w'):  # Безопасно закрывает всё
        for t in range(len(GraphTime)):
            print(GraphTime[t], Et[t], St[t], Tt[t], Tdt[t], Nl[t], Nr[t], file=MegaFile)
        MegaFile.close()
        plt.close()


    return (sc,)
