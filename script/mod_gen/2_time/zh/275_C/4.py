def main():
    S = []
    for i in range(9):
        S.append(input())
    result = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i == 0 or i == 8:
                    if j == 0 or j == 8:
                        result += 1
                    else:
                        if S[i][j-1] == '.' or S[i][j+1] == '.':
                            result += 1
                elif j == 0 or j == 8:
                    if S[i-1][j] == '.' or S[i+1][j] == '.':
                        result += 1
                else:
                    if S[i-1][j] == '.' or S[i+1][j] == '.' or S[i][j-1] == '.' or S[i][j+1] == '.':
                        result += 1
    print(result)

if __name__ == '__main__':
    main()