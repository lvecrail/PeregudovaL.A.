n=int(input("Введите число: "))
i=0
while pow(2, i)<=n:
    i+=1
    print(i-1, pow(2, i)//2)

