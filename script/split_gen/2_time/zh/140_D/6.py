def main():
    n, k = map(int, input().split())
    s = input()
    # 左端点为l，右端点为r
    l = 0
    r = 0
    # 从左向右扫描，找到第一个L
    while l < n and s[l] == 'R':
        l += 1
    # 从右向左扫描，找到第一个R
    while r < n and s[n-r-1] == 'L':
        r += 1
    # 从左向右扫描，找到所有的R的左端点
    rr = []
    i = l
    while i < n:
        while i < n and s[i] == 'L':
            i += 1
        if i == n:
            break
        j = i
        while j < n and s[j] == 'R':
            j += 1
        rr.append((i, j))
        i = j
    # 从右向左扫描，找到所有的L的右端点
    ll = []
    i = n-r-1
    while i >= 0:
        while i >= 0 and s[i] == 'R':
            i -= 1
        if i < 0:
            break
        j = i
        while j >= 0 and s[j] == 'L':
            j -= 1
        ll.append((j+1, i+1))
        i = j
    # print(l, r)
    # print(rr)
    # print(ll)
    # 求出左右两边的人数
    ans = r + l
    # 求出中间的人数
    for i in range(len(rr)):
        ans += rr[i][1] - rr[i][0]
        if i > 0:
            ans += rr[i][0] - rr[i-1][1] - 1
    for i in range(len(ll)):
        ans += ll[i][1] - ll[i][0]
        if i > 0:
            ans += ll[i][0] - ll[i-1][1] - 1
    # print(ans)
    # 从左向右
