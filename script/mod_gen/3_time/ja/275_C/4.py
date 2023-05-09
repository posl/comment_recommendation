def main():
    S = [input() for _ in range(9)]
    cnt = 0
    for i in range(9):
        for j in range(9):
            if i <= 6 and j <= 6:
                if S[i][j] == S[i+1][j] == S[i][j+1] == S[i+1][j+1] == "#":
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()