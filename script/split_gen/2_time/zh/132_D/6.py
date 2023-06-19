def C(n, m):
    if n == m:
        return 1
    elif m == 1:
        return n
    else:
        return C(n-1, m-1) + C(n-1, m)
n, k = map(int, input().split())
for i in range(k):
    print(C(n-k+1, i+1) * C(k-1, i) % (10**9+7))
