n=int(input("Введите число:"))
if n>1 and n<9:
    for i in range(1, n+1):
        for e in range(1, i+1):
            print(e, sep="", end="")
        print()