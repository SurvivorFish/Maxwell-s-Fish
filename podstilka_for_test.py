import Base
from Base import m, w, h, dt, canvas


# podstilka is some magic code, that hides here. So, main looks beautiful.



# Some constants
# I'm hope, that I measure everything in СГС


# List of spheres creation
N = 200 # Количество частиц
V = 10 # Какая-то характерная скорость частиц
R = 5 # Радиус частиц
Sprs = Base.createSpheresList(N, R, V)  # List of spheres creation
E_0 = Base.Energy(Sprs, m)  # Calculating its energy

# IDK, its kostil, Im stupid
DS = []  # List of spheres for drawing
for i in range(len(Sprs)):  # Drawing spheres on canvas
    s = Sprs[i]
    DS.append([s.ts, i])


# I guess, main fiziks logic
# But now it looks awful
# I will rewrite it one day (maybe, I hope, I want)
def physics_step():
    # Считаем физику для каждой сферы
    for s in DS:  # DS is hard (kostilic) object, that contain:
        sp = s[0]  # s[0] is sphere object on tkinter's canvas
        i = s[1]  # s[1] is sphere index

        # Collisions - Колизеи
        # Checking if someone can collide with us
        b = canvas.find_overlapping(Sprs[i].x - Sprs[i].r, Sprs[i].y - Sprs[i].r, Sprs[i].x + Sprs[i].r,
                                 Sprs[i].y + Sprs[i].r)
        # Checking if someone is located near us
        if len(b) > 1:  # At least one always exists. We are simply located near us.
            # Choosing right second object of collision
            if b[0] - 1 != i:
                j = b[0] - 1  # bad tkinter indexation
            else:
                j = b[1] - 1

            # Vector of collision
            rx = Sprs[i].x - Sprs[j].x
            ry = Sprs[i].y - Sprs[j].y
            # Py-thagoras
            if rx ** 2 + ry ** 2 < 4 * Sprs[i].r ** 2:
                # Calculating velocities after collision
                bi = Base.bubuh(Sprs[i].Vx, Sprs[i].Vy, Sprs[j].Vx, Sprs[j].Vy, rx, ry)
                Sprs[i].Vx = bi[0]
                Sprs[i].Vy = bi[1]
                Sprs[j].Vx = bi[2]
                Sprs[j].Vy = bi[3]

        # Moving object on canvas
        canvas.move(sp, Sprs[i].Vx * dt, Sprs[i].Vy * dt)
        # Rewriting object's data about position
        Sprs[i].x = Sprs[i].x + Sprs[i].Vx * dt
        Sprs[i].y = Sprs[i].y + Sprs[i].Vy * dt
        # Asking the sphere not to go away
        if Sprs[i].x + Sprs[i].r >= w or Sprs[i].x - Sprs[i].r <= 0:
            Sprs[i].Vx = -Sprs[i].Vx
        if Sprs[i].y + Sprs[i].r >= h or Sprs[i].y - Sprs[i].r <= 0:
            Sprs[i].Vy = -Sprs[i].Vy
        # Maxwell's Fish

        if abs(Sprs[i].x - 400) <= Sprs[i].Vx*dt:
            if (Sprs[i].Vx < 0 and Sprs[i].Vy < 0 and abs(Sprs[i].Vx) > abs(Sprs[i].Vy)) or (
                    Sprs[i].Vx > 0 and Sprs[i].Vy > 0 and abs(Sprs[i].Vx) < abs(Sprs[i].Vy)):
                Sprs[i].Vx, Sprs[i].Vy = Sprs[i].Vy, Sprs[i].Vx
            if (Sprs[i].Vx < 0 and Sprs[i].Vy > 0 and abs(Sprs[i].Vx) > abs(Sprs[i].Vy)) or (
                    Sprs[i].Vx > 0 and Sprs[i].Vy < 0 and abs(Sprs[i].Vx) < abs(Sprs[i].Vy)):
                Sprs[i].Vx, Sprs[i].Vy = -Sprs[i].Vy, -Sprs[i].Vx
            else:
                Sprs[i].Vx = -Sprs[i].Vx
