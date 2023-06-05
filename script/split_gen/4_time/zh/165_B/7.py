def f(x):
    y = 100
    for i in range(10**18):
        y = int(y * 1.01)
        if y >= x:
            return i+1
x = int(input())
print(f(x))
