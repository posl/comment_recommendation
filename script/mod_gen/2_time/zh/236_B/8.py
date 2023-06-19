def solve(n, a):
    from collections import Counter
    c = Counter(a)
    for k, v in c.items():
        if v == 1:
            return k

if __name__ == '__main__':
    solve()