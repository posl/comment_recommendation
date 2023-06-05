def problems286_c():
    n, a, b = map(int, input().split())
    s = input()
    if n % 2 == 0:
        if a > b:
            print((a * n) + b)
        else:
            print((a * n) + (b * (n // 2)))
    else:
        if a > b:
            print((a * n) + b)
        else:
            print((a * n) + (b * (n // 2)) + a)
