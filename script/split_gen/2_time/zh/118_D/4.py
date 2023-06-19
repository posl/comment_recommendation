def main():
    # 输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 全排列
    a.sort(reverse=True)
    # 从最大的数字开始，每次减去一个数字，直到数字用完
    ans = []
    while n > 0:
        for i in range(m):
            if n - a[i] >= 0:
                ans.append(a[i])
                n -= a[i]
                break
    # 输出
    for i in range(len(ans)):
        print(ans[i], end='')
