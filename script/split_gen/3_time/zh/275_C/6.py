def main():
    s = []
    for i in range(9):
        s.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                continue
            if i - 1 >= 0 and j - 1 >= 0 and s[i - 1][j - 1] == '.':
                continue
            if i - 1 >= 0 and s[i - 1][j] == '.':
                continue
            if i - 1 >= 0 and j + 1 < 9 and s[i - 1][j + 1] == '.':
                continue
            if j - 1 >= 0 and s[i][j - 1] == '.':
                continue
            if j + 1 < 9 and s[i][j + 1] == '.':
                continue
            if i + 1 < 9 and j - 1 >= 0 and s[i + 1][j - 1] == '.':
                continue
            if i + 1 < 9 and s[i + 1][j] == '.':
                continue
            if i + 1 < 9 and j + 1 < 9 and s[i + 1][j + 1] == '.':
                continue
            ans += 1
    print(ans)
