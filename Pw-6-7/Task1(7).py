lst=[1,-2,-2,-3, 4, 4, -7,-8,-8, 9]
for i in range(len(lst)-1):
    print(lst[i], lst[i+1]) if lst[i]<0 and lst[i+1]<0 else None