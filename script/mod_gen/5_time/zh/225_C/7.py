def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    a = [[(i - 1) * 7 + j for j in range(1, 8)] for i in range(1, 10 ** 100 + 1)]
    for i in range(10 ** 100):
        for j in range(7):
            if a[i][j] == b[0][0]:
                if m == 1:
                    print('Yes')
                    return
                if n == 1:
                    print('Yes')
                    return
                if m == 2 and n == 2:
                    if a[i][j + 1] == b[0][1] and a[i + 1][j] == b[1][0] and a[i + 1][j + 1] == b[1][1]:
                        print('Yes')
                        return
                if m == 3 and n == 2:
                    if a[i][j + 1] == b[0][1] and a[i][j + 2] == b[0][2] and a[i + 1][j] == b[1][0] and a[i + 1][j + 1] == b[1][1] and a[i + 1][j + 2] == b[1][2]:
                        print('Yes')
                        return
                if m == 4 and n == 2:
                    if a[i][j + 1] == b[0][1] and a[i][j + 2] == b[0][2] and a[i][j + 3] == b[0][3] and a[i + 1][j] == b[1][0] and a[i + 1][j + 1] == b[1][1] and a[i + 1][j + 2] == b[1][2] and a[i + 1][j + 3] == b[1][3]:
                        print('Yes')
                        return
                if m == 5 and n == 2:
                    if a[i][j + 1] == b[0][1] and a[i][j + 2] == b[0][

if __name__ == '__main__':
    main()