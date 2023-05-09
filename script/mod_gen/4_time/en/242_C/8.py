def main():
    n = int(input())
    a = [[0 for i in range(9)] for j in range(n)]
    for i in range(n):
        for j in range(9):
            if i == 0:
                a[i][j] = 1
            elif j == 0:
                a[i][j] = a[i-1][j] + a[i-1][j+1]
            elif j == 8:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j] + a[i-1][j+1]
    print(a[n-1][0]%998244353)

if __name__ == '__main__':
    main()