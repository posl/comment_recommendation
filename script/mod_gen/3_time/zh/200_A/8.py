def problems200_a():
    n = int(input())
    if n % 100 == 0:
        print(n // 100)
    else:
        print(n // 100 + 1)
problems200_a()
