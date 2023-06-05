def main():
    # 读取输入
    N = int(input().strip())
    # 初始化
    ans = 0
    # 逐位判断
    while N > 0:
        # 逢三进一
        ans += (N + 2) // 3
        # 去掉最后三位
        N //= 10
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()