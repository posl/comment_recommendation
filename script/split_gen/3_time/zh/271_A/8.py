def hexa(n):
    a = n // 16
    b = n % 16
    if a < 10:
        a = str(a)
    elif a == 10:
        a = 'A'
    elif a == 11:
        a = 'B'
    elif a == 12:
        a = 'C'
    elif a == 13:
        a = 'D'
    elif a == 14:
        a = 'E'
    else:
        a = 'F'
    if b < 10:
        b = str(b)
    elif b == 10:
        b = 'A'
    elif b == 11:
        b = 'B'
    elif b == 12:
        b = 'C'
    elif b == 13:
        b = 'D'
    elif b == 14:
        b = 'E'
    else:
        b = 'F'
    return a+b
n = int(input())
print(hexa(n))
