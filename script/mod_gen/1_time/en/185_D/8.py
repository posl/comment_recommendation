def solve(N, M, A):
    # N: number of squares
    # M: number of blue squares
    # A: list of blue squares
    # return: minimum number of uses of the stamp needed to have no white square.
    if M == 0:
        return 1
    A = [0] + A + [N + 1]
    B = []
    for i in range(M + 1):
        B.append(A[i + 1] - A[i] - 1)
    maxB = max(B)
    if maxB == 0:
        return 0
    B.sort()
    B = B[1:]
    minB = B[0]
    for i in range(1, M):
        minB = gcd(minB, B[i])
    return (maxB + minB - 1) // minB

if __name__ == '__main__':
    solve()