def main():
    S = []
    for i in range(9):
        S.append(input())
    cnt = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i + 1 < 9 and j + 1 < 9:
                    if S[i][j + 1] == '#' and S[i + 1][j] == '#' and S[i + 1][j + 1] == '#':
                        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()