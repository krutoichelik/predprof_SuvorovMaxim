import csv

f = open(file="space.txt")
f2 = open("space_uniq_password.csv", "w")
# считываем файлы
sps = []

for i in f:
    sps.append(i.replace("\n", "").split("*"))  # переносим данные из файлов в список

sps = sps[1::]

for i in sps:
    _index = i[0].index("-")

    password = (i[0][_index - 3] + i[0][_index - 2] + i[0][_index - 1] + i[0][2] + i[0][1] + i[1][2] + i[1][1] + i[1][
        0]).upper()  # создание пароля

    i.append(password)
    f2.write("*".join(i) + "\n")
