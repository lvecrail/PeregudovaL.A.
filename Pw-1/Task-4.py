sds=int(input("Введите количество секунд: "))
min=sds//60
hr=min//60
day=hr//24
print(day, ":" , hr, ":", min, ":", sds )