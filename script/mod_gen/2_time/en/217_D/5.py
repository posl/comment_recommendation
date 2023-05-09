def solve():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            print(cuts[cuts.index(x) + 1] - cuts[cuts.index(x) - 1])

if __name__ == '__main__':
    solve()