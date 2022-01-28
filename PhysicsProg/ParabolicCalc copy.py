import math

print(f"If you do not know a certain value leave it blank\nplease use m/s for velocity, meters for position, and seconeds for time\nand m/s^2 for acceleration.")
y = False
while y == False:
    try:
        vx0 = float(input("Please enter the starting x velocity: "))
        y = True
        if vx0 == '':
            vx0 = False
    except:
        print("Must use a number, floating point values are accepted.")

y = False
while y == False:
    try:
        vxf = float(input("Please enter the final x velocity: "))
        y = True
        if vxf == '':
            vxf = False
    except:
        print("Must use a number, floating point values are accepted.")

y = False
while y == False:
    try:
        x0 = float(input("Please enter the starting x position: "))
        y = True
        if x0 == '':
            x0 = False
    except:
        print("Must use a number, floating point values are accepted.")

y = False
while y == False:
    try:
        xf = float(input("Please enter the final x position: "))
        y = True
        if xf == '':
            xf = False
    except:
        print("Must use a number, floating point values are accepted.")

y = False
while y == False:
    try:
        ax = float(input("Please enter the acceleration of x: "))
        y = True
        if ax == '':
            ax = False
    except:
        print("Must use a number, floating point values are accepted.")

y = False
while y == False:
    try:
        t = float(input("Please enter total time of system: "))
        y = True
        if t == '':
            t = False
    except:
        print("Must use a number, floating point values are accepted.")

y = False
while y == False:
    try:
        vy0 = float(input("Please enter the starting y velocity: "))
        y = True
        if vy0 == '':
            vy0 = False
    except:
        print("Must use a number, floating point values are accepted.")

y = False
while y == False:
    try:
        vyf = float(input("Please enter the final y velocity: "))
        y = True
        if vyf == '':
            vyf = False
    except:
        print("Must use a number, floating point values are accepted.")

y = False
while y == False:
    try:
        y0 = float(input("Please enter the starting y position: "))
        y = True
        if y0 == '':
            y0 = False
    except:
        print("Must use a number, floating point values are accepted.")

y = False
while y == False:
    try:
        yf = float(input("Please enter the final y position: "))
        y = True
        if yf == '':
            yf = False
    except:
        print("Must use a number, floating point values are accepted.")
ay = -9.8

ParaBolValue = "Vx0={0}m/s, Vxf={1}m/s, X0={2}m, Xf={3}m, Ax={4}m/s^2, Vy0={5}m/s,\nVyf={6}m/s, Y0={7}m, Yf={8}m, Ay={9}m/s^2, t={10}seconds."
print(ParaBolValue.format(vx0, vxf, x0, xf, ax, vy0, vyf, y0, yf, ay, t))