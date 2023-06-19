def main():
    # 读入数据
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    # 计算答案
    ans = 0
    for i in range(k):
        if i == k - 1:
            ans += n - a[i] + 1
        else:
            ans += a[i + 1] - a[i]
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()