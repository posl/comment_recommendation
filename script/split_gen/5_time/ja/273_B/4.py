def problems273_b():
    x,k = map(int,input().split())
    for _ in range(k):
        if x%10 == 0:
            x //= 10
        else:
            x -= 1
    print(x)
