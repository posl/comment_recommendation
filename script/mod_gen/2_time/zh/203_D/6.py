def main():
    #读入数据
    n,k = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    #计算每个区域的高度
    s = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            s[i+1][j+1] = s[i][j+1] + s[i+1][j] - s[i][j] + a[i][j]
    #判断是否存在一个区域，使得其内部的方块高度的中位数是最低的
    def check(x):
        t = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                t[i+1][j+1] = t[i][j+1] + t[i+1][j] - t[i][j] + (1 if a[i][j] > x else 0)
        for i in range(n-k+1):
            for j in range(n-k+1):
                if t[i+k][j+k] - t[i][j+k] - t[i+k][j] + t[i][j] >= (k*k+1)//2:
                    return True
        return False
    #二分查找
    left = -1
    right = 10**9 + 1
    while right - left > 1:
        mid = (left + right)//2
        if check(mid):
            right = mid
        else:
            left = mid
    print(right)

if __name__ == '__main__':
    main()