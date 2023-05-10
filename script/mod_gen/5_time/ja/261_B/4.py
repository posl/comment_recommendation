def main():
    n = int(input())
    a = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] == 'W' or a[j][i] == 'D':
                    continue
                else:
                    print('incorrect')
                    exit()
            elif a[i][j] == 'L':
                if a[j][i] == 'L' or a[j][i] == 'D':
                    continue
                else:
                    print('incorrect')
                    exit()
            elif a[i][j] == 'D':
                if a[j][i] == 'D':
                    continue
                else:
                    print('incorrect')
                    exit()
    print('correct')
    return
main()

if __name__ == '__main__':
    main()