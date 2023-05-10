def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += 10
        for j in range(10):
            if S[i][j] == str((ans // 10) % 10):
                ans -= 1
                break
    print(ans)
