def solve():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#':
                if S[i - 1][j] == '.':
                    ans += 1
                if S[i + 1][j] == '.':
                    ans += 1
                if S[i][j - 1] == '.':
                    ans += 1
                if S[i][j + 1] == '.':
                    ans += 1
    if ans == 0:
        print(0)
    else:
        print(ans // 2 + 1)

if __name__ == '__main__':
    solve()