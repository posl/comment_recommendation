def problems278_a():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(0)
        del A[0]
    print(' '.join(map(str, A)))
