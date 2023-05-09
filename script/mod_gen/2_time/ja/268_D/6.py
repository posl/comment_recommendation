def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(1, N):
        S[i] = '_' + S[i]
    ans = ''.join(S)
    if ans in T:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    solve()