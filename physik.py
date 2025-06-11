import numpy as np 
from parameter import N, karton_breite, karton_lange, dt, grenze_v
lage = np.random.rand(N, 2) * [karton_lange, karton_breite]
gwkeit = np.random.randn(N, 2) * 300


def tritt():
    global lage, gwkeit, karton_breite, karton_lange
    lage += dt * gwkeit
    print("lage[0]:", lage[0])
    for i in range(N):
        gw = np.linalg.norm(gwkeit[i])
        x, y = lage[i]
        v_x = gwkeit[i,0]
        v_y = gwkeit[i,1]
    if y <= 0 or y >= karton_breite:
        gwkeit[i, 1] *= -1
    if x <= 0 or x >= karton_lange:
        gwkeit[i,0] *= -1
    elif abs(x - karton_lange / 2) < 0.01:
        
        vx = gwkeit[i, 0]
    if vx > 0 and gw < grenze_v :
        pass  # медленные проходят слева направо
    elif vx < 0 and gw > grenze_v:
        pass  # быстрые проходят справа налево
    else:
        gwkeit[i, 0] *= -1  # остальные отражаются
    




