#Elís Orri

from random import *

print("1: Danskeppni")
print("2: Símanúmer")
print("3: Bekkur")
val = int(input("Hvað villtu gera? "))

#Liður 1

if val == 1:
    #Forrit býr til 2 tuplur
    herrar = ("Kalli", "Palli", "Lalli", "Halli", "Jói", "Gói")
    domur = ("Lína", "Stína", "Bína", "Nína", "Dísa", "Lísa")
    #Forrit birtir tuplurnar
    print("Herrarnir eru:", herrar[:])
    print("Dömurnar eru:", domur[:])
    por = []
    #Forrit parar saman pörin
    for i in range(6):
        par = (herrar[i], "og", domur[i])
        por.append(par)
    print("Pörin eru:", por)
    #Forrit býr til random par
    herra = herrar[randint(0,5)]
    dama = domur[randint(0,5)]
    print("Parið er", herra, "og", dama)
    #Forrit býr til 6 random pör þar sem engin manneskja er í meira en einu pari
    randlisti1, randlisti2 = sample(range(6), 6), sample(range(6),6)
    for i in range(6):
        print("%s og %s" % (herrar[randlisti1[i]], domur[randlisti2[i]]))
    #Forrit finnur nöfn með staf af vali notenda í sér
    stafur = input("Sláðu inn staf ")
    print("Nöfnin með", stafur, "í sér eru:")
    for i in range(6):
        if stafur in herrar[i]:
            print(herrar[i])
        if stafur in domur[i]:
            print(domur[i])
    #Forrit finnur nöfn sem byrja á staf af vali notenda
    stafur = input("Sláðu inn stóran staf ")
    print("Nöfnin sem byrja á", stafur, "eru:")
    for i in range(6):
        if stafur in herrar[i][0]:
            print(herrar[i])
        if stafur in domur[i][0]:
            print(domur[i])
    #Forrit finnur nöfn með fleiri en eitt l í nafninu
    print("Nöfn með fleiri en 1 l í nafninu:")
    for i in range(6):
        teljari = 0
        for x in range(len(herrar[i])):
            if "l" in herrar[i][x]:
                teljari = teljari + 1
            if teljari == 2:
                print(herrar[i])
                teljari = teljari + 1
    for i in range(6):
        teljari = 0
        for x in range(len(domur[i])):
            if "l" in domur[i][x]:
                teljari = teljari + 1
            if teljari == 2:
                print(domur[i])
                teljari = teljari + 1

#Liður 2

if val == 2:
    nöfn = ("Kalli", "Palli", "Lalli", "Halli", "Jói", "Gói", "Lína", "Stína", "Bína", "Nína")
    simaNumer = (6459856, 8649856, 8948264, 8651234, 6655896, 6985698, 8984568, 8794526, 6667895, 8985798)
    