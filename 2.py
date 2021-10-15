import math
print("Programm küsib teilt ringi raadiuse ning tagastab ringi pindala ja ümbermöödu")
rad = float(input("Sisestage ringi raadius (cm): "))
#print(rad)
c = 2 * math.pi * rad
c = round(c, 2)
c = str(c)
#print(c)
s = math.pi * (rad*rad)
s = round(s, 2)
s = str(s)
#print (s)

print("Ringi pindala on:", s, "cm2 ja ümbermõõt", c, "cm.")