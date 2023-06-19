def main():
    s = []
    for i in range(9):
        s.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i + 1 < 9 and j + 1 < 9 and s[i + 1][j] == '#' and s[i][j + 1] == '#' and s[i + 1][j + 1] == '#':
                    ans += 1
    print(ans)
