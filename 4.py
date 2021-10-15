#Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni).
# (muutuja - variable, tingimus - condition, if-lause - if statement)

n1 = int(input("Sisesta esimene arv: "))
n2 = int(input("Sisesta teine arv: "))
if n1 > n2 : 
    n2=str(n2)   
    print("Teie poolt sisestatud arvude miinimum on:", n2)
else:
    n1=str(n1)
    print("Teie poolt sisestatud arvude miinimum on:", n1)