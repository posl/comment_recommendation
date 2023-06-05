def problem161_c():
    n,k = map(int,input().split())
    while n >= k:
        n = n % k
    print(n)
