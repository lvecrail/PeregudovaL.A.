from random import randint
import json


def p(c, d):
    n = json.load(open("peregudova_ly_y_222_vvod_ex-1.txt", "r"))
    result = []

    for i in range(len(n)):
        for j in range(len(n[i])):
            if (n[i][j] == c):
                result.append(i)

    for i in range(len(result)):
        for j in range(len(n[result[i]])):
            n[result[i]][j] *= d

    file = open("peregudova_ly_y_222_vvod_ex-1.txt", "w")
    file.writelines(json.dumps(n))


def writeToFile():
    x = generator(int(input())), int(input(), int(input()), int(input()))

    file = open("peregudova_ly_y_222_vvod_ex-1.txt", "w")
    file.writelines(json.dumps(x))


def generator(column, maxValue, minValue):
    rowA = []
    for i in range(rowA):

        for f in range(column):
            column.append((maxValue, minValue))

        rowA.append(column)

    return rowA


writeToFile()