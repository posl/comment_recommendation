def main():
    # 读入数据
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 统计各个值的个数
    cnt = [0] * m
    for i in range(n):
        cnt[a[i]] += 1
    # 从小到大依次取出
    ans = 0
    for i in range(m):
        # 两个相邻的值之间的差值
        d = cnt[i] - cnt[(i + 1) % m]
        # 如果差值大于0，就从前面的值取出差值个数的牌
        if d > 0:
            ans += d
            cnt[(i + 1) % m] += d
        # 如果差值小于0，就从后面的值取出差值个数的牌
        elif d < 0:
            ans += -d * (m - 1)
            cnt[(i + 1) % m] += d * (m - 1)
    print(ans)

if __name__ == '__main__':
    main()