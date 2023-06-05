def main():
    n = int(input())
    if n == 1:
        print('1')
    elif n == 2:
        print('1')
        print('1 1')
    else:
        a = [[0 for i in range(n)] for i in range(n)]
        a[0][0] = 1
        a[1][0] = 1
        a[1][1] = 1
        for i in range(2, n):
            a[i][0] = 1
            a[i][i] = 1
            for j in range(1, i):
                a[i][j] = a[i-1][j-1] + a[i-1][j]
        for i in range(n):
            for j in range(i+1):
                print(a[i][j], end=' ')
            print()

if __name__ == '__main__':
    main()