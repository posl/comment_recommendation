def problem161_c():
    n, k = map(int, input().split())
    print(min(n % k, k - n % k))
problem161_c()
