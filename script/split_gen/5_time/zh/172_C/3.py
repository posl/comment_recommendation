def main():
    # 读入数据
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # 计算前缀和
    for i in range(1,n):
        a[i] += a[i-1]
    for i in range(1,m):
        b[i] += b[i-1]
    # 答案
    ans = 0
    # 遍历所有可能的读书数量
    for i in range(n+1):
        # j是从B桌读书的数量
        j = 0
        # 从A桌读书的数量为i
        # 从B桌读书的数量为j
        # 从A桌读书的时间为a[i-1]分钟
        # 从B桌读书的时间为b[j-1]分钟
        # 从A桌读书的时间+a桌读书的时间<=k
        # 从B桌读书的时间+b桌读书的时间<=k
        # 从A桌读书的数量<=n
        # 从B桌读书的数量<=m
        # 从A桌读书的数量+从B桌读书的数量<=n+m
        # 从A桌读书的数量+从B桌读书的数量<=n+m
        # 从A桌读书的数量+从B桌读书的数量<=n+m
        if a[i-1] > k:
            break
        while j <= m and b[j-1] > k - a[i-1]:
            j += 1
        ans = max(ans,i+j-1)
    print(ans)
