def problem281_c():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    t = t%n
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum >= t:
            print(i+1,t)
            break
    return
problem281_c()
