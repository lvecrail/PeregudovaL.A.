n=int(input("Введите число: "))
m=int(input("Введите число: "))
k=int(input("Введите число: "))
if k<n*m and ((k%n==0) or (k%m==0)):
    print("Да")
else:
        print("Нет")