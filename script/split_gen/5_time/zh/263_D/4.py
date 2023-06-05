def solve(N, L, R, A):
    # print(N, L, R, A)
    # print('A', A)
    # print('L', L)
    # print('R', R)
    # print('L + R', L + R)
    # print('A + L + R', A + L + R)
    # print('min(A + L + R)', min(A + L + R))
    return sum(A) + min(A + L + R) * (N - 2)
