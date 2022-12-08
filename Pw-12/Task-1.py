def division(n, b):
    if n < b:
        return n
    return division(n - b, b)
print(division(274, 5))