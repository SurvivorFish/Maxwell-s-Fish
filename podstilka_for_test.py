import math
import tkinter
import tkinter as tk
import Base

# podstilka is some magic code, that hides here. So, main looks beautiful.


# Setting up Tkinter
fps = 120  # frames per second. Physics time resolution is also fps
dt = 1 / fps
w = 800  # Window width
h = 600  # Window height
lin = tk.Tk()  # Setting up tkinter
lin.title("Our Super Program 1")
lin.geometry(f'{w}x{h}')
can = tkinter.Canvas(lin)
can.configure(bg="white")
can.pack(fill="both", expand=True)

# Some constants
# I'm hope, that I measure everything in СГС
k = 1.38 * 10 ** -16  # Bolcman's postoyannaya
R = 2
N = 100
V = 10
m = 6.65 * 10 ** -24  # mass of molecule of He

# List of spheres creation
Sprs = Base.createSpheresList(N, R, V)  # List of spheres creation
E_0 = Base.Energy(Sprs, m)  # Calculating its energy

# IDK, its kostil, Im stupid
DS = []  # List of spheres for drawing
for i in range(len(Sprs)):  # Drawing spheres on canvas
    s = Sprs[i]
    DS.append([can.create_oval(s.x - s.r, s.y - s.r, s.x + s.r, s.y + s.r, fill="blue", outline="Black", width=1), i])


# I guess, main fiziks logic
# But now it looks awful
# I will rewrite it one day (maybe, I hope, I want)
def physics_step():
    for s in DS:  # DS is hard (kostilic) object, that contain:
        sp = s[0]  # s[0] is sphere object on tkinter's canvas
        i = s[1]  # s[1] is sphere index

        # Collisions - Колизеи
        # Checking if someone can collide with us
        b = can.find_overlapping(Sprs[i].x - Sprs[i].r, Sprs[i].y - Sprs[i].r, Sprs[i].x + Sprs[i].r,
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
        can.move(sp, Sprs[i].Vx * dt, Sprs[i].Vy * dt)
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
