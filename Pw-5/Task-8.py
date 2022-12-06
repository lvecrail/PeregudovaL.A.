a=-1
b=0
c=0
n=int(input("Введите число: "))
while n!=0:
    if a==n:
        b+=1
    else:
        a=n
        c=max(c, b)
        b=1
    n=int(input("Введите число: "))
c=max(c, b)
print(c)



