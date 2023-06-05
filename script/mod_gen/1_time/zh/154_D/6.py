def main():
    # 读入数据
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # 计算答案
    s = sum(p[:k])
    ans = s
    for i in range(k, n):
        s += p[i] - p[i-k]
        ans = max(ans, s)
    # 打印答案
    print((ans + k) / 2)

if __name__ == '__main__':
    main()