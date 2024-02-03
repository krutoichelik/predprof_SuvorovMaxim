f = open(file="space.txt")  # открываем файл
sps = []

for i in f:
    sps.append(i.replace("\n", "").split("*"))  # переносим данные из файлов в список

sps = sps[1::]

while True:
    flag = False
    a = input()
    if a == "stop":
        break  # останавливаем ввод по команде stop

    for i in sps:
        if i[0] == a:
            print(f"Корабль {i[0]} был отправлен с планеты: {i[1]} и его направление движения было: {i[-1]}")
            flag = True
            break
    # проверка на наличие планеты
    if not (flag):
        print("error.. er.. ror..")
