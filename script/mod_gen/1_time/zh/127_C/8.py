def solve():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_, r_ = map(int, input().split())
        l.append(l_)
        r.append(r_)
    print(max(0, min(r) - max(l) + 1))

if __name__ == '__main__':
    solve()