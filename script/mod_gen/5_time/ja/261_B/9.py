def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    print('incorrect')
                    return
            if a[i][j] == 'L':
                if a[j][i] != 'W':
                    print('incorrect')
                    return
            if a[i][j] == 'D':
                if a[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')
main()

if __name__ == '__main__':
    main()