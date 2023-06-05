def main():
    S = []
    for i in range(9):
        S.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i > 0 and j > 0 and S[i-1][j-1] == '#':
                    if i > 0 and S[i-1][j] == '#':
                        if j > 0 and S[i][j-1] == '#':
                            count += 1
    print(count)

if __name__ == '__main__':
    main()