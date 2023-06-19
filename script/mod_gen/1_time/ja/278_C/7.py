def main():
    N, Q = map(int, input().split())
    f = [set() for i in range(N)]
    for i in range(Q):
        t, a, b = map(lambda x: int(x) - 1, input().split())
        if t == 0:
            f[a].add(b)
            f[b].add(a)
        elif t == 1:
            f[a].discard(b)
            f[b].discard(a)
        else:
            print('Yes' if f[a] & f[b] else 'No')
main()
