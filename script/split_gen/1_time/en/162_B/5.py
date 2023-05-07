def fizzbuzz(n):
    a, b, c = 0, 0, 0
    for i in range(1, n+1):
        if i % 3 == 0:
            a += i
        if i % 5 == 0:
            b += i
        if i % 15 == 0:
            c += i
    return a + b - c
