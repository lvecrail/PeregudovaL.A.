yr=int(input("Введите год: "))
if yr%4!=0:
    print("нет")
elif yr%100==0:
    if yr%400==0:
        print("Да")
    else:
        print("Нет")
else:
    print("Да")
