def main():
    # 读入数据
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 从左到右累积和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    # 计算每个余数的个数
    cnt = [0] * m
    for i in range(n + 1):
        cnt[s[i] % m] += 1
    # 计算答案
    ans = 0
    for i in range(m):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)
