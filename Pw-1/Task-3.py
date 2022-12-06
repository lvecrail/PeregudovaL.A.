name=str(input("Введите ваше имя: "))
if name==("Иван"):
    print("Неверно")
age=int(input("Введите ваш возраст: "))
if age<75 and age>16:
    print("Поздравляем вы поступили в ВГУИТ!")
elif age<16 and age>0:
    print("Сначала нужно окончить школу!") 
    age=int(input("Введите свой возраст ещё раз: "))
    if 16-age>=2 and 16-age<=4:
        print("Ещё" ,16-age, "года  учиться в школе")
    elif 16-age==1:
        print("Ещё" ,16-age, "год  учиться в школе")
    16-age<=5 and 16-age<=15
    print("Ещё" ,16-age, "лет  учиться в школе")