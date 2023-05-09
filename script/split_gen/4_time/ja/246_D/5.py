def main():
    n = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    if n == 0:
        print(0)
        return
    for i in range(1000):
        if i**3 > n:
            a = i
            break
    for i in range(1000):
        if (a-1)**3 + i**3 > n:
            b = i
            break
    for i in range(1000):
        if (a-1)**3 + (b-1)**3 + i**3 > n:
            c = i
            break
    for i in range(1000):
        if (a-1)**3 + (b-1)**3 + (c-1)**3 + i**3 > n:
            d = i
            break
    for i in range(1000):
        if (a-1)**3 + (b-1)**3 + (c-1)**3 + (d-1)**3 + i**3 > n:
            e = i
            break
    print((a-1)**3 + (b-1)**3 + (c-1)**3 + (d-1)**3 + (e-1)**3)
    return
