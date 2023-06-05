def main():
    # 读取输入
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # 排序
    p.sort()
    # 计算结果
    ans = 0
    for i in range(k):
        ans += p[i]
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()