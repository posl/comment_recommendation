def main():
    #input
    S = []
    for i in range(9):
        S.append(input())
    #solve
    ans = 0
    for i in range(7):
        for j in range(7):
            if S[i][j] == '#' and S[i+1][j] == '#' and S[i][j+1] == '#' and S[i+1][j+1] == '#':
                ans += 1
    #output
    print(ans)

if __name__ == '__main__':
    main()