n=int(input("Введите число: "))
sum=0
i=0
average=0
while n!=0:
    sum+=n
    n=int(input("Введите число: "))
    i+=1
average=(sum/i)
print(average)