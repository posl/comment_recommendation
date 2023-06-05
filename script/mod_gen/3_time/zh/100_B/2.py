def problems100_b():
    a = input().split()
    d = int(a[0])
    n = int(a[1])
    if d == 0:
        if n == 100:
            print(101)
        else:
            print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(100*n)
    else:
        if n == 100:
            print(1010000)
        else:
            print(10000*n)
problems100_b()
