def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    T.sort(key=len)
    T = [t.replace('_', '') for t in T]
    T = set(T)
    for s in S:
        if s not in T:
            print(s)
            return
    print(-1)

if __name__ == '__main__':
    solve()