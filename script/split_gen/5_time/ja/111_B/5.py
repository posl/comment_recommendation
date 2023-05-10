def problems111_b():
    n = int(input())
    x = 100
    for i in range(10):
        if n <= x:
            print(x)
            break
        x += 111
