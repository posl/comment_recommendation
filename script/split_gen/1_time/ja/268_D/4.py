def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(3, 17):
        for c in product(S, repeat=i):
            s = "".join(c)
            if s in T:
                continue
            if len(s) != len(set(s)):
                continue
            print(s)
            return
    print(-1)
