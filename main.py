import math
import time
import Base
from Base import m, k, dt, lin, T
from podstilka_for_test import physics_step, Sprs, N

# Main body
Zero = time.time()  # Время начала работы программы
E_0 = Base.Energy(Sprs, m)
S_0 = Base.Entropy(Sprs, m)
while True:
    start = time.time()  # Время начала этого шага
    t = start - Zero  # Текущее время с начала работы программы

    # Считаем физику
    physics_step()

    # Считаем энергию и энтропию
    E = Base.Energy(Sprs, m)
    S = Base.Entropy(Sprs, m) - S_0
    print("=========================")
    print((E-N*k*T)/(N*k*T))
    dS = N*k*math.log(2)
    print(S/dS)
    print("=========================")

    lin.update()  # Обновляем графику
    end = time.time()  # time of the end of this step
    time_delta = end - start  # time spent on this step
    if time_delta < dt:  # waiting the rest of the step for constant time delta
        time.sleep(dt - time_delta)
    else:
        print("Ваш комп не справляется с достаточно быстрым подсчётом. Убавьте FPS")
