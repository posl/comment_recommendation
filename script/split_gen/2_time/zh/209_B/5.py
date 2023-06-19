def problems209_b():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if i % 2 == 1:
            count += a[i] - 1
        else:
            count += a[i]
    if count > x:
        print("No")
    else:
        print("Yes")
