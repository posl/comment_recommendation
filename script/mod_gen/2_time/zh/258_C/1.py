def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input())))
    # print(a)
    # print(a[0][0])
    # print(a[1][1])
    # print(a[2][2])
    # print(a[3][3])
    # print(a[0][3])
    # print(a[1][2])
    # print(a[2][1])
    # print(a[3][0])
    maxnum = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                maxnum = max(maxnum,a[i][j]+a[i+1][j]+a[i][j+1]+a[i+1][j+1])
            elif i == 0 and j == n-1:
                maxnum = max(maxnum,a[i][j]+a[i+1][j]+a[i][j-1]+a[i+1][j-1])
            elif i == n-1 and j == 0:
                maxnum = max(maxnum,a[i][j]+a[i-1][j]+a[i][j+1]+a[i-1][j+1])
            elif i == n-1 and j == n-1:
                maxnum = max(maxnum,a[i][j]+a[i-1][j]+a[i][j-1]+a[i-1][j-1])
            elif i == 0:
                maxnum = max(maxnum,a[i][j]+a[i][j-1]+a[i][j+1]+a[i+1][j]+a[i+1][j-1]+a[i+1][j+1])
            elif i == n-1:
                maxnum = max(maxnum,a[i][j]+a[i][j-1]+a[i][j+1]+a[i-1][j]+a[i-1][j-1]+a[i-1][j+1])
            elif j == 0:
                maxnum = max(maxnum,a[i][j]+a[i-1][j]+a[i+1][j]+a[i][j+1]+a[i-1][j+1]+a[i+1][j+1])
            elif j == n-1:

if __name__ == '__main__':
    main()