def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(3, 17):
        for s in product(S, repeat=i):
            s = ''.join(s)
            if len(s) != i: continue
            if s in T: continue
            print(s)
            return
    print(-1)

if __name__ == '__main__':
    solve()