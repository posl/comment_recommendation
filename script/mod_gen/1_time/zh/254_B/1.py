def main():
    n = int(input())
    a = [[0 for i in range(n)] for i in range(n)]
    a[0][0] = 1
    for i in range(1,n):
        for j in range(i+1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j],end=' ')
        print()

if __name__ == '__main__':
    main()