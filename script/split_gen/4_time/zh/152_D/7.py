def main():
    # 读入
    N = int(input())
    # 初始化
    ans = 0
    # 遍历
    for i in range(1, N + 1):
        # 求一下最后一位
        last = i % 10
        # 如果最后一位是0，那么就跳过
        if last == 0:
            continue
        # 求一下第一位
        first = int(str(i)[0])
        # 如果第一位也是0，那么也跳过
        if first == 0:
            continue
        # 如果满足条件，那么就加一
        if last == first:
            ans += 1
    # 打印
    print(ans)
main()
