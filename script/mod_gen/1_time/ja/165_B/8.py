def calc(x):
    y = 100
    i = 0
    while y < x:
        y = int(y*1.01)
        i += 1
    print(i)
x = int(input())
calc(x)
