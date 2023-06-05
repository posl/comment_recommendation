def problem142_a():
    n = int(input())
    if n % 2 == 0:
        print(0.5)
    else:
        print((n // 2 + 1) / n)
problem142_a()
