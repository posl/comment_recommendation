def problems246_b():
    import math
    A, B = map(int, input().split())
    x = (A**2 + B**2) ** 0.5
    y = math.atan(B/A)
    print(x*math.cos(y), x*math.sin(y))
problems246_b()
