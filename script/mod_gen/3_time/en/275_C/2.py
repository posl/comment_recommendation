def main():
    S = []
    for i in range(9):
        S.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#" and i+1 < 9 and j+1 < 9 and S[i+1][j] == "#" and S[i][j+1] == "#" and S[i+1][j+1] == "#":
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()