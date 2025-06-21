import time

import matplotlib.pyplot as plt
from parameter import w, h, r, dt, alpha, doGraph, doPrint
from Base import molecule_list, Energy, Entropy, Temperature, E_0, S_0
from Maxwell_demon import dimon
import keyboard

if doGraph:
    time0 = time.time()
    # Массивы для графиков
    GraphTime = []
    Et = []
    St = []
    Tt = []
    MegaFile = open('Graph data/Data.txt', 'w')

Demons_Entropy = 0

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
    coords.clear()
    xs.clear()
    ys.clear()

    # Цикл, обрабатывающий физику для каждой молекулы
    for molecule in molecule_list:
        # отражения от границ
        if molecule.x <= r or molecule.x >= w - r:
            molecule.Vx = -molecule.Vx
        if molecule.y <= r or molecule.y >= h - r:
            molecule.Vy = -molecule.Vy

        can_move, Demons_Entropy = dimon(molecule, Demons_Entropy)

        if can_move:
            # Обновление координат молекул
            molecule.x = molecule.x + molecule.Vx * dt / alpha
            molecule.y = molecule.y + molecule.Vy * dt / alpha

        # Обновление списков для MathPlotLib
        x = molecule.x
        y = molecule.y
        xs.append(x)
        ys.append(y)
        coords.append([x, y])

        # Если уж не выводим в отельный файл
        if doPrint:  # Пишу энергию, энтропию
            print(Entropy() - S_0, Entropy() - S_0 + Demons_Entropy)
    if doGraph:
        GraphTime.append(time.time() - time0)
        Et.append(Energy())
        St.append(Entropy())
        Tt.append(Temperature())


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
    if keyboard.is_pressed('q'):  # Безопасно закрывает всё
        for t in range(len(GraphTime)):
            print(GraphTime[t], Et[t], St[t], Tt[t], file=MegaFile)
        MegaFile.close()
        plt.close()


    return (sc,)
