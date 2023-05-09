def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if all(S[i][k] == 'x' and S[j][k] == 'x' for k in range(M)):
                continue
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()