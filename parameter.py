import numpy as np 
N = 100 #количество частиц
karton_breite = 3 #ширина коробки
karton_lange = 9 #длина коробки
grenze_v = 150 #средняя скорость (тип *100км/с)
dt = 0.01 #шаг по времени
lage = np.random.rand(N, 2) * [karton_lange, karton_breite]
gwkeit = np.random.randn(N, 2) * 300
