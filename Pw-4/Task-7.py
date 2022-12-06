rs=1
sum=0
n=int(input("Введите число: "))
for i in range(1, n+1):
    rs*=i
    sum+=rs
    print(sum)