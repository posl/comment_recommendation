def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    print('incorrect')
                    return
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    print('incorrect')
                    return
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')

if __name__ == '__main__':
    main()