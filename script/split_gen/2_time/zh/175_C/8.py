def problems175_c():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x >= k*d:
        print(x-k*d)
    else:
        k = k - x//d
        x = x%d
        if k%2 == 0:
            print(x)
        else:
            print(d-x)
