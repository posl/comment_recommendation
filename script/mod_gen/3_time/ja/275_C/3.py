def main():
    S = []
    for i in range(9):
        S.append(input())
    cnt = 0
    for i in range(9):
        for j in range(9):
            if i+1 < 9 and j+1 < 9 and i-1 >= 0 and j-1 >= 0:
                if S[i][j] == '#' and S[i+1][j] == '#' and S[i-1][j] == '#' and S[i][j+1] == '#' and S[i][j-1] == '#':
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()