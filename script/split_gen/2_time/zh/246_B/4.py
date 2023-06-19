def problem246_b():
    A, B = map(int, input().split())
    x = (A**2 + B**2 - 1) / (2*A)
    y = (A**2 + B**2 - 1) / (2*B)
    print(x, y)
