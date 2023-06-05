def problem248_b():
    a,b,k = map(int, input().split())
    c = 0
    while a < b:
        a = a * k
        c = c + 1
    print(c)
