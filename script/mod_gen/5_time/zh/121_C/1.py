def main():
    # 读入数据
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照价格升序排序
    ab.sort()
    # 贪心算法
    ans = 0
    for a, b in ab:
        if m <= b:
            ans += a * m
            break
        else:
            ans += a * b
            m -= b
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()