def main():
    S = [input() for _ in range(9)]
    ans = 0
    for r in range(9):
        for c in range(9):
            if S[r][c] == '#':
                # 右下
                if r + 1 < 9 and c + 1 < 9:
                    if S[r][c + 1] == '#' and S[r + 1][c] == '#' and S[r + 1][c + 1] == '#':
                        ans += 1
                # 左下
                if r + 1 < 9 and c - 1 >= 0:
                    if S[r][c - 1] == '#' and S[r + 1][c] == '#' and S[r + 1][c - 1] == '#':
                        ans += 1
                # 右上
                if r - 1 >= 0 and c + 1 < 9:
                    if S[r - 1][c] == '#' and S[r][c + 1] == '#' and S[r - 1][c + 1] == '#':
                        ans += 1
                # 左上
                if r - 1 >= 0 and c - 1 >= 0:
                    if S[r - 1][c] == '#' and S[r][c - 1] == '#' and S[r - 1][c - 1] == '#':
                        ans += 1
    print(ans)
