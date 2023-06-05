def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    # 从大到小排序
    a.sort(reverse=True)
    bc.sort(key=lambda x: x[1], reverse=True)
    # 从大到小取得最大值
    ans = 0
    j = 0
    for i in range(n):
        if j < m and a[i] < bc[j][1]:
            ans += bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
        else:
            ans += a[i]
    print(ans)
