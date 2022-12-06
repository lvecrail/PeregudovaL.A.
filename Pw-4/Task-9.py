sum=0
n=int(input("Введите число:"))
x=0
y=1
for i in range(2, n+1):
    sum+=y
    c=y
    y+=x
    x=c
    print(sum)