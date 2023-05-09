def f(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return (b - a + 1) // 2 % 2
    elif a % 2 == 0 and b % 2 != 0:
        return (b - a + 2) // 2 % 2
    elif a % 2 != 0 and b % 2 == 0:
        return (b - a) // 2 % 2
    else:
        return (b - a + 1) // 2 % 2
