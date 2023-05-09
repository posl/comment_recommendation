def problems101_c():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    if (n-1) % (k-1) == 0:
        ans = (n-1) // (k-1)
    else:
        ans = (n-1) // (k-1) + 1
    print(ans)
