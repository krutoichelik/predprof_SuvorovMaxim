f = open(file="space.txt")
f2 = open(file="space_new.txt", mode="w") #считываем файлы

sps = []
output = []

for i in f:
    sps.append(i.replace("\n", "").split("*")) #переносим данные из файлов в список

sps = sps[1::]

for j in range(len(sps)):
    i = sps[j]

    n = int(i[0][i[0].index("-") + 1])
    m = int(i[0][i[0].index("-") + 2])
    t = len(i[1])

    xd = int(i[-1].split(" ")[0])
    yd = int(i[-1].split(" ")[1])
    #считываем значения, из которых состоит формула в отдельные переменные для удобства

    if n > 5:
        x = n + xd
    else:
        x = (n + xd) * -4 + t

    if m > 3:
        y = m + t + yd
    else:
        y = (n + yd) * -1 * m
        #составление формул

    if i[0][i[0].index("-") - 1] == "V":
        output.append(f"{i[0]} - ({x}, {y})")
        #записываем все подходящие планеты в список

f2.writelines("\n".join(output)) #выводим содержимое списка в файл
