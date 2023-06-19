def problems204_c():
    N, M = map(int, input().split())
    # 0 <= M <= min(2000, N(N-1))
    # 0 <= M <= N(N-1)
    # 0 <= M <= N^2 - N
    # M <= N^2 - N
    # M + N <= N^2
    # N^2 - N - M >= 0
    # N^2 - N - M = 0
    # N = (1 + sqrt(1 + 4M)) / 2
    # N = (1 - sqrt(1 + 4M)) / 2
    # N = 1/2 + sqrt(1/4 + M)
    # N = 1/2 - sqrt(1/4 + M)
    # 0.5 + sqrt(0.25 + M) >= 0
    # sqrt(0.25 + M) >= -0.5
    # 0.25 + M >= 0
    # M >= -0.25
    # M >= 0
    # 0.5 - sqrt(0.25 + M) >= 0
    # sqrt(0.25 + M) <= 0.5
    # 0.25 + M <= 0.25
    # M <= 0
    if M > N * (N - 1):
        return
    if M < 0:
        return
    # 2 <= N <= 2000
    # 2 <= N <= 2000
    if N < 2:
        return
    if N > 2000:
        return
    # 1 <= A_i, B_i <= N
    # 1 <= A_i, B_i <= N
    # A_i != B_i
    # A_i != B_i
    # (A_i, B_i) are different
    # (A_i, B_i) are different
    # 1 <= A_i, B_i <= N
    # 1 <= A_i, B_i <= N
    # A_i != B_i
    # A_i != B_i
    # (A_i, B_i) are different
    # (A_i, B_i) are different
    # 1 <=
