def problems246_c():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        if A[i] - X > 0:
            total += X
        else:
            total += A[i]
    print(total)
