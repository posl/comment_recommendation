def problems246_b():
    a, b = map(int, input().split())
    x = b / (a ** 2 + b ** 2) ** 0.5
    y = a / (a ** 2 + b ** 2) ** 0.5
    print(x, y)
problems246_b()
