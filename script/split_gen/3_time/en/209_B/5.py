def problems209_b():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if i % 2 == 1:
            s += a[i] - 1
        else:
            s += a[i]
    if s <= x:
        print("Yes")
    else:
        print("No")
