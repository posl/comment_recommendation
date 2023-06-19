def get_max_score(A, N, M, Q, a, b, c, d):
    max_score = 0
    for i in range(1, 2**N):
        A = [int(x) for x in bin(i)[2:]]
        A = [0] * (N - len(A)) + A
        if sum(A) == 0:
            continue
        score = 0
        for j in range(Q):
            if A[b[j] - 1] - A[a[j] - 1] == c[j]:
                score += d[j]
        max_score = max(max_score, score)
    return max_score
