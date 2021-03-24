#Zadanie1
# lista1 = [0+x for x in range(1, 31, 1)]
# lista2 = [str(x*2) for x in lista1]
# plik = open("liczyx2.txt", "w")
# plik.writelines(lista2)

#Zadanie2
# plik = open("liczyx2.txt", "r")
# odczyt = plik.readlines()
#  print(odczyt)

#Zadanie3
# with open("tekst.txt", "w") as plik2:
#     for newLine in range(10) :
#         plik2.write("hehe\n")
# with open("tekst.txt", "r") as plik2:
#     for line in plik2:
#         print(line, end="")

#Zadanie4
# produkt = NaZakupy.NaZakupy("Bannany", 8, "Kg", 0.8)
# produkt.wyswietl_Produkt()
# produkt.ile_produktu()
# print(produkt.ile_kosztuje())

#Zadanie5
# ciag = CiagiAry.CiagiAry()
# ciag.pobierz_elementy(2, 4, 20)
# ciag.policz_elementy()
# ciag.pobierz_elementy(4, 6, 15)
# ciag.policz_sume()
# ciag.wyświetl_dane()

#Zadanie6
# robaczek = Robaczek.Robaczek()
# robaczek.whereAmI()
# robaczek.goUp(2)
# robaczek.whereAmI()
# robaczek.goRight(3)
# robaczek.whereAmI()
# robaczek.goDown(8)
# robaczek.whereAmI()
# robaczek.goLeft(10)
# robaczek.whereAmI()