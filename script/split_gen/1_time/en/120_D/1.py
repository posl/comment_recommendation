def main():
    N, M = [int(x) for x in input().split()]
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = [int(x) for x in input().split()]
    # Find the number of bridges between each pair of islands
    # (1, 2) and (2, 1) are considered the same.
    # The number of bridges between (i, j) is denoted by bridges[i][j].
    bridges = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        bridges[A[i]][B[i]] += 1
        bridges[B[i]][A[i]] += 1
    # Find the number of pairs of islands (a, b) (a < b) that we can travel between using some of the bridges remaining.
    # The number of pairs is denoted by pairs[i][j].
    pairs = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            pairs[i][j] = pairs[i][j - 1] + bridges[i][j]
    # Find the number of pairs of islands (a, b) (a < b) that we can travel between using some of the bridges remaining.
    # The number of pairs is denoted by pairs[i][j].
    pairs = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            pairs[i][j] = pairs[i][j - 1] + bridges[i][j]
    # Find the inconvenience just after the i-th bridge collapses.
    # The inconvenience is denoted by inconvenience[i].
    inconvenience = [0] * (M + 1)
    for i in range(1, M + 1):
        inconvenience[i] = inconvenience[i - 1] + pairs[A[i - 1]][B[i - 1]]
    # Print the inconvenience just after the i-th bridge collapses.
    for i in range(1, M
