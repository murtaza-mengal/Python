import math
print("Pysics\nChapter Sound\nEchos")
T1 = 273
T2 = float(input("Current Tempareture: "))
v1 = 330
v2 = math.sqrt(T2+273/T1) * v1
t = float(input("Time : "))
print((v2*t/2) , " meter")
print("Minimum distance to hear echoes")