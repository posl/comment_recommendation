def problems101_c():
    n,k = map(int, input().split())
    A = list(map(int, input().split()))
    res = 0
    for i in range(n-k+1):
        res += min(A[i:i+k])
    print(res)
