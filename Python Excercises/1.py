print("Programm teisendab Teie Eesti kroonid Eurodeks")

eek = int(input("Sisestage summa (EEK): "))
#print(eek)

x = eek / 15.6
#print(x)
eur = round(x, 0)
eur = int(eur)
eur = str(eur)
#print(eur)

print (eek, "EEK =", eur, "EURi")