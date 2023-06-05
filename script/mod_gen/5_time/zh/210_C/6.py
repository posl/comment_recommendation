def main():
    # 读入数据
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    # 预处理
    colors = [0] * (10**9 + 1)
    for i in range(k):
        colors[c[i]] += 1
    # 双指针
    ans = 0
    for i in range(10**9 + 1):
        if colors[i] > 0:
            ans += 1
    for i in range(k, n):
        colors[c[i - k]] -= 1
        if colors[c[i - k]] == 0:
            ans -= 1
        colors[c[i]] += 1
        if colors[c[i]] == 1:
            ans += 1
    # 结果
    print(ans)

if __name__ == '__main__':
    main()