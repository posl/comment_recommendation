def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i > 0 and j > 0:
                    if S[i - 1][j] == '#' and S[i][j - 1] == '#' and S[i - 1][j - 1] == '#':
                        ans += 1
                if i > 0 and j < 8:
                    if S[i - 1][j] == '#' and S[i][j + 1] == '#' and S[i - 1][j + 1] == '#':
                        ans += 1
                if i < 8 and j > 0:
                    if S[i + 1][j] == '#' and S[i][j - 1] == '#' and S[i + 1][j - 1] == '#':
                        ans += 1
                if i < 8 and j < 8:
                    if S[i + 1][j] == '#' and S[i][j + 1] == '#' and S[i + 1][j + 1] == '#':
                        ans += 1
    print(ans // 4)
