def main():
    n = int(input())
    result = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if result[i][j] == 'W':
                if result[j][i] != 'L':
                    print('incorrect')
                    return
            if result[i][j] == 'L':
                if result[j][i] != 'W':
                    print('incorrect')
                    return
            if result[i][j] == 'D':
                if result[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')

if __name__ == '__main__':
    main()