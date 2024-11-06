#1.pole s 5 stringovými hodnotami

pole = ["ostrov", "kolotoč", "kometa", "Zapletal", "obr"]
print("základní pole:", pole)


#2.prvek vítr pomocí metody append

pole.append("vítr")
print("po přidání vítr:", pole)


#3.Odstranění druhého prvku z pole pomocí metody remove

pole.remove(pole[1]) 
print("po odstranění druhého prvku:", pole)


#4.Zaměnění 5. hodnotu v poli za slunce

pole[4] = "slunce"
print("po zaměnění 5. hodnoty za slunce:", pole)


#5.Přidání 2 stringových hodnot pomocí metody extend

pole.extend(["nakladak", "kamion"])
print("po přidání nakladak  kamion:", pole)