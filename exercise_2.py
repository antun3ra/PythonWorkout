def mysum(*args):
    sum = 0
    for v in args:
        sum += v
    return sum


test = mysum(8, 9, 10, -15, 20)

print(test)
