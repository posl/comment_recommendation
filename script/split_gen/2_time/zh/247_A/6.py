def func(n):
    x = 0
    while True:
        if n <= x:
            break
        x += 1
        for a in range(x):
            for b in range(x):
                if x == a**3 + a**2*b + a*b**2 + b**3:
                    return x
n = int(input())
print(func(n))
