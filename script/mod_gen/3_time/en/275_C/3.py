def solve():
    S = []
    for _ in range(9):
        S.append(input())
    ans = 0
    for i in range(8):
        for j in range(8):
            if S[i][j] == '#' and S[i+1][j] == '#' and S[i][j+1] == '#' and S[i+1][j+1] == '#':
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()