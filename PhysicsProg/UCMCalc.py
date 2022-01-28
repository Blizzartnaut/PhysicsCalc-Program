import math

#newtons laws of motion
def UCMCalc():
    end = False
    while end == False:
        which1 = False
        which1 = input(f"What variable are you looking for?\nType a for Centrepital Acceleration, type v for change in Velocity,\n type t for Time: ")
        if which1 == 'a' or which1 == 'A' or which1 == 'acceleration' or which1 == 'Acceleration':
            print("Calculating Centripetal Acceleration; use numbers in m/s for veloctiy, m/s2 for acceleration and s, seconds for time.")
            y = False
            while y == False:
                try:
                    v1 = float(input("Change in Veloctiy of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            y = False
            while y == False:
                try:
                    t1 = float(input("Time in seconds of rotation of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            #using m1, a1 as in later versions of this program more inputs will be allowed as determined by user
            a1 = v1*t1
            CentrepitalAccValue = "a-> = {0}m/s * {1}s = {2}m/s^2"
            print(CentrepitalAccValue.format(v1,t1,a1))
            end = True

        elif which1 == 'v' or which1 == 'V' or which1 == 'velocity' or which1 == 'Velocity':
            print("Calculating Centripetal Acceleration; use numbers in m/s for veloctiy, m/s2 for acceleration and s, seconds for time.")
            y = False
            while y == False:
                try:
                    a1 = float(input("Centripetal Acceleration of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            y = False
            while y == False:
                try:
                    t1 = float(input("Time of Rotation of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            #using a1 as in later versions of this program more inputs will be allowed as determined by user
            v1 = a1 * t1
            CentrepitalAccValue = "a-> = {0}m/s * {1}s = {2}m/s^2"
            print(CentrepitalAccValue.format(v1,t1,a1))
            end = True


        elif which1 == 't' or which1 == 'T' or which1 == 'time' or which1 == 'Time':
            print("Calculating Centripetal Acceleration; use numbers in m/s for veloctiy, m/s2 for acceleration and s, seconds for time.")
            y = False
            while y == False:
                try:
                    a1 = float(input("Centrepital Acceleration of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            y = False
            while y == False:
                try:
                    v1 = float(input("Change in Velocity of object: "))
                    y = True
                except:
                    print("Must use a number, floating point values are allowed")
            #using a1 as in later versions of this program more inputs will be allowed as determined by user
            t1 = a1 / v1
            CentrepitalAccValue = "a-> = {0}m/s * {1}s = {2}m/s^2"
            print(CentrepitalAccValue.format(v1,t1,a1))
            end = True

        elif which1 == 'end' or which1 == 'End' or which1 == 'e' or which1 == 'E' or which1 == 'q' or which1 == 'Q' or which1 == 'Quit' or which1 == 'quit':
            end = True
            print('Goodbye')

        else:
            print("Im sorry but your respone doesnt seem valid.")