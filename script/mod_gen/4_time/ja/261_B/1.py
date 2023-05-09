def main():
    n = int(input())
    a = [list(input()) for _ in range(n)]
    for i in range(n):
        a[i][i] = '-'
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] == 'W' or a[j][i] == 'D':
                    print('incorrect')
                    exit()
            elif a[i][j] == 'L':
                if a[j][i] == 'L' or a[j][i] == 'D':
                    print('incorrect')
                    exit()
            elif a[i][j] == 'D':
                if a[j][i] == 'W' or a[j][i] == 'L':
                    print('incorrect')
                    exit()
    print('correct')

if __name__ == '__main__':
    main()