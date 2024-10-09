import random

#první úkol (Vytvoří pole, ve kterém bude uloženo 9 číselných hodnot, které budou přeházená (0-100).)
array1 = [random.randint(0, 100) for _ in range(9)]
print(array1)

#druhý úkol (Vypiše první, prostřední a poslední hodnotu pole)
print("první hodnota", array1[0])
print("prostřední hodnota", array1[int(len(array1)/2)])
print("poslední hodnota", array1[-1])

#třetí úkol (Zaměňí 5 indexovou hodnotu pole za číslo 34.)
array1[5]=34

#čtvrtý úkol (Vypiše indexově 7 hodnotu z pole.)
print(array1[6])

#pátý úkol (Vypiše délku pole.)
print(len(array1))

#šestý úkol (Vypiše minimální a maximální hodnotu pole.)
print(max(array1))
print(min(array1))

#sedmý úkol (Vytvoří druhé pole s libovolnými čísly a libovolnou délkou.)
array2 = [random.randint(0, 100) for _ in range(9)]
print(array2)

#osmý úkol (Sečte pole a vypište je.)
print(sum(array2))

#devátý úkol (Sečte indexově 1 a 5 hodnotu z pole č.2.)
součet = array2[0] + array2[4]
print(součet)
