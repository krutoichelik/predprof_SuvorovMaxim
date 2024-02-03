f = open(file="space.txt")

data = {}

sps = []

for i in f:
    sps.append(i.replace("\n", "").split("*"))  # переносим данные из файлов в список

sps = sps[1::]

for i in sps:
    if i[1] not in data:
        data[i[1]] = [i[0]]
    else:
        zxc = data[i[1]]
        zxc.append(i[0])
        data[i[1]] = zxc

        # составление словаря

print(data)  # вывод словаря
