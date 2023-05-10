def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += 10
        for j in range(10):
            if S[i][j] == str((i+j)%10):
                ans -= 1
                break
    print(ans)

if __name__ == '__main__':
    solve()