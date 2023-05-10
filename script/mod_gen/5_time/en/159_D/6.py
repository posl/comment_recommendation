def solve(N, A):
    from collections import defaultdict
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    s = 0
    for a in A:
        s += d[a] - 1
    return s

if __name__ == '__main__':
    solve()