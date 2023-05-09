def problems175_c():
    x,k,d = map(int, input().split())
    x = abs(x)
    if x//d > k:
        print(x-k*d)
    else:
        if (x//d)%2 == k%2:
            print(x%d)
        else:
            print(d-x%d)
