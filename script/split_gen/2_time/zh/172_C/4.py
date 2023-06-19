def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #累计时间
    for i in range(n-1):
        a[i+1] += a[i]
    for i in range(m-1):
        b[i+1] += b[i]
    
    #枚举A桌读书本数
    ans = 0
    for i in range(n):
        if a[i] > k:
            break
        #二分查找B桌读书本数
        ok = m
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if b[mid] > k - a[i]:
                ok = mid
            else:
                ng = mid
        ans = max(ans, i + ok + 2)
    #枚举B桌读书本数
    for i in range(m):
        if b[i] > k:
            break
        #二分查找A桌读书本数
        ok = n
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if a[mid] > k - b[i]:
                ok = mid
            else:
                ng = mid
        ans = max(ans, i + ok + 2)
    
    print(ans)
