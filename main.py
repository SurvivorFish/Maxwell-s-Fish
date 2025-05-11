import math
import time

import Base
from podstilka_for_test import physics_step, lin, dt, Sprs, E_0, m, k, N

# Main body
Zero = time.time()  # time of the very beginning
while True:
    start = time.time()  # time of the start of this step
    t = start - Zero  # Current time (from the very beginning)

    # Physics step
    physics_step()


    """
    # Energy and entropy measuring
    E = Base.Energy(Sprs, m)
    S = N * k * math.log(E / E_0)
    print(S)
    """


    lin.update()  # Updating the window
    end = time.time()  # time of the end of this step
    time_delta = end - start  # time spent on this step
    if time_delta < dt:  # waiting the rest of the step for constant time delta
        time.sleep(dt - time_delta)
