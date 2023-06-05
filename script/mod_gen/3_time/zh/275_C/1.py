def main():
    S = []
    for i in range(9):
        S.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i <= 7 and j <= 7:
                    if S[i + 1][j] == '#' and S[i][j + 1] == '#' and S[i + 1][j + 1] == '#':
                        count += 1
                if i >= 1 and j >= 1:
                    if S[i - 1][j] == '#' and S[i][j - 1] == '#' and S[i - 1][j - 1] == '#':
                        count += 1
                if i <= 7 and j >= 1:
                    if S[i + 1][j] == '#' and S[i][j - 1] == '#' and S[i + 1][j - 1] == '#':
                        count += 1
                if i >= 1 and j <= 7:
                    if S[i - 1][j] == '#' and S[i][j + 1] == '#' and S[i - 1][j + 1] == '#':
                        count += 1
    print(count)

if __name__ == '__main__':
    main()