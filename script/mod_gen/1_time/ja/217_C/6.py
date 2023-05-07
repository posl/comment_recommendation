def solve(n, p):
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    return q

if __name__ == '__main__':
    solve()