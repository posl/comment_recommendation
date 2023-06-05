def problem175_c():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x >= k*d:
        print(x-k*d)
    else:
        y = x//d
        if (k-y)%2 == 0:
            print(x%d)
        else:
            print(abs(x%d-d))
