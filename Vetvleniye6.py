ferzh = input("Координаты ферзя: ")
peshka = input("Координаты пешки: ")
columns = 'ABCDEFGH'
stolbes_ferzh = columns.index(ferzh[0]) + 1 # метод index() находит порядковый номер символа в строке
stroka_ferzh = int(ferzh[1])
stolbes_peshka = columns.index(peshka[0]) + 1
stroka_peshka = int(peshka[1])
if stolbes_ferzh == stolbes_peshka or stroka_ferzh == stroka_peshka or (stolbes_ferzh - stolbes_peshka) == (stroka_ferzh - stroka_peshka):
    print("ооба")
else:
    print("жок")
'''or
true or true - true
true or false - true
false or false - false
false or true - true'''