def prob208_c():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if k>=n:
        if k%n==0:
            print(k//n)
        else:
            print(k//n+1)
        return
    else:
        b = k
        for i in range(n):
            if a[i]<b:
                b = a[i]
        print(b)
        return
prob208_c()
