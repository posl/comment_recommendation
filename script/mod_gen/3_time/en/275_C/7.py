def main():
    S = [[0]*9 for i in range(9)]
    for i in range(9):
        S[i] = input()
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i-1 >= 0 and j-1 >= 0 and S[i-1][j] == '#' and S[i][j-1] == '#' and S[i-1][j-1] == '#':
                    ans += 1
                if i-1 >= 0 and j+1 <= 8 and S[i-1][j] == '#' and S[i][j+1] == '#' and S[i-1][j+1] == '#':
                    ans += 1
                if i+1 <= 8 and j-1 >= 0 and S[i+1][j] == '#' and S[i][j-1] == '#' and S[i+1][j-1] == '#':
                    ans += 1
                if i+1 <= 8 and j+1 <= 8 and S[i+1][j] == '#' and S[i][j+1] == '#' and S[i+1][j+1] == '#':
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()