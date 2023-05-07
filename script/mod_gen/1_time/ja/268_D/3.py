def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(3, 17):
        for j in range(3 ** i):
            s = ""
            for k in range(i):
                s += S[(j // (3 ** k)) % 3]
            if s not in T:
                print(s)
                return
    print(-1)

if __name__ == '__main__':
    solve()