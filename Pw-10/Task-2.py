from random import randint
import json 

def p():
    n = json.load(open("peregudova_ly_y_222_vvod_ex-1.txt", "r"))
    maxSum = 0
    line = -1

    for i in range(len(n)):
        lS = 0
        for j in range(len(n[i])):
            if line == i:
                continue

            if n[i][j] % 2 == 0:
                line = i
            else:
                lS += my_abs(n[i][j])

        if lS > maxSum:
            maxSum = lS 
            line = i

    file = open("peregudova_ly_y_222_vvod_ex-1.txt", "w")
    file.writelines(f"{line},{maxSum}")

def my_abs(a):
    #return a if a > 0 else -a
    if a > 0:
        return a
    else:
        return -a
def writeToFile():
    x = generator(int(input())),int(input(),int(input()),int(input()))
    
    file = open("peregudova_ly_y_222_vvod_ex-1.txt", "w")
    file.writelines(json.dumps(x))

def generator(r, c, m, min):
    rA = []
    for i in range(r):
        cA = []
        for f in range(c):
            cA.append(randint(m,min))
            
        rA.append(cA)

    return rA

writeToFile()
p()