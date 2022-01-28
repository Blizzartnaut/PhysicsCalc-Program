import math
import ForceCalc
import UCMCalc

'''This is a test case to see if i understand physics enough to be able to program a series of calculators,
 which may eventually culminate into a webapp calculator'''
print("There are multiple calculators you can use, which one do you choose?")
print("For the Force Calculator, type A. For the Uniform Circular Motion Calculator, type B.")
choose = input("Type what calculator you want to use: ")
if choose == 'A' or choose == 'a':
    ForceCalc.ForceCalc()

elif choose == 'b' or choose == 'B':
    UCMCalc.UCMCalc()

else:
    print("Goodbye")