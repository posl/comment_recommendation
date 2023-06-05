def solve(K, N, A):
    A.sort()
    # 最初の点からの距離
    dist = [0]
    for i in range(N-1):
        dist.append(A[i+1] - A[i])
    # 最後の点からの距離
    dist.append(K - A[N-1] + A[0])
    return K - max(dist)
