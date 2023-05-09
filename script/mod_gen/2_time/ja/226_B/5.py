def solve(N, L, A):
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N):
        d[tuple(A[i])] += 1
    return len(d)

if __name__ == '__main__':
    solve()