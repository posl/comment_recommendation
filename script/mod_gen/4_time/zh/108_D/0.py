def solve(L):
    N = 20
    M = 60
    u = [0] * M
    v = [0] * M
    w = [0] * M
    # 1. 1->2->3->...->N
    for i in range(N - 1):
        u[i] = i + 1
        v[i] = i + 2
        w[i] = 0
    # 2. 1->2->3->...->N->1->2->3->...->N
    for i in range(N - 1, 2 * N - 2):
        u[i] = i + 1 - (N - 1)
        v[i] = i + 2 - (N - 1)
        w[i] = i - (N - 1) + 1
    # 3. 1->2->3->...->N->1->2->3->...->N->1->2->3->...->N
    for i in range(2 * N - 2, 3 * N - 4):
        u[i] = i + 1 - 2 * (N - 1)
        v[i] = i + 2 - 2 * (N - 1)
        w[i] = 2 * (i - 2 * (N

if __name__ == '__main__':
    solve()