def problem246_c():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n):
        if x <= 0:
            break
        if a[i] < x:
            a[i] = 0
            x -= 1
    print(sum(a))
problem246_c()
