def problem127_a():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(int(b/2))
    else:
        print(0)
problem127_a()
