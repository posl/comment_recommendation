def get_permutation(N, K, P):
    # 順列を数値に変換
    P = list(map(lambda x: int(x) - 1, P))
    # 順列を数値に変換
    Q = list(range(N))
    # 順列を数値に変換
    R = list(range(N))
    # 順列を数値に変換
    for i in range(N):
        Q[P[i]] = i
    # 順列を数値に変換
    for i in range(N):
        R[Q[i]] = i
    # 順列を数値に変換
    for i in range(K - 1):
        # 順列を数値に変換
        for j in range(N - 1):
            # 順列を数値に変換
            if R[j] < R[j + 1]:
                # 順列を数値に変換
                R[j], R[j + 1] = R[j + 1], R[j]
                # 順列を数値に変換
                Q[R[j]], Q[R[j + 1]] = Q[R[j + 1]], Q[R[j]]
    return Q

if __name__ == '__main__':
    get_permutation()