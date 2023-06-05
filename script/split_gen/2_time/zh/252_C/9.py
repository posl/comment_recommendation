def problems252_b():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(k):
        a[b[i]-1] = 0
    print("Yes" if max(a)>0 else "No")
