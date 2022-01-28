import math

#newtons laws of motion
def ForceCalc():
    end = False
    while end == False:
        which1 = False
        which1 = input(f"What variable are you looking for?\nType F for Force, type m for mass, type a for acceleration: ")
        if which1 == 'F' or which1 == 'f' or which1 == 'Force' or which1 == 'force':
            print("Calculating Force; use numbers in kilograms for mass, m/s2 for acceleration and Newtons for force.")
            y = False
            while y == False:
                try:
                    m1 = float(input("Mass of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            y = False
            while y == False:
                try:
                    a1 = float(input("Acceleration of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            #using m1, a1 as in later versions of this program more inputs will be allowed as determined by user
            f = m1*a1
            ForceVal = "F = {0}kg * {1}m/s^2 = {2}N"
            print(ForceVal.format(m1,a1,f))
            end = True

        elif which1 == 'm' or which1 == 'M' or which1 == 'Mass' or which1 == 'mass':
            print("Calculating Mass; use numbers in kilograms for mass, m/s2 for acceleration and Newtons for force.")
            y = False
            while y == False:
                try:
                    f = float(input("Force of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            y = False
            while y == False:
                try:
                    a1 = float(input("Acceleration of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            #using a1 as in later versions of this program more inputs will be allowed as determined by user
            m1 = f / a1
            ForceVal = "F = {0}kg * {1}m/s^2 = {2}N"
            print(ForceVal.format(m1,a1,f))
            end = True


        elif which1 == 'a' or which1 == 'A' or which1 == 'acceleration' or which1 == 'Acceleration':
            print("Calculating Acceleration; use numbers in kilograms for mass, m/s2 for acceleration and Newtons for force.")
            y = False
            while y == False:
                try:
                    f = float(input("Force of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            y = False
            while y == False:
                try:
                    m1 = float(input("Mass of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            #using a1 as in later versions of this program more inputs will be allowed as determined by user
            a1 = f / m1
            ForceVal = "F = {0}kg * {1}m/s^2 = {2}N"
            print(ForceVal.format(m1,a1,f))
            end = True

        elif which1 == 'end' or which1 == 'End' or which1 == 'e' or which1 == 'E' or which1 == 'q' or which1 == 'Q' or which1 == 'Quit' or which1 == 'quit':
            end = True
            print('Goodbye')

        else:
            print("Im sorry but your respone doesnt seem valid.")