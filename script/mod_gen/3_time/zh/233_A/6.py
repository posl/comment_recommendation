def main():
    # 读取输入
    x, y = map(int, input().split())
    # 计算差额
    diff = y - x
    # 计算最少需要贴多少张10元的邮票
    print(diff // 10)

if __name__ == '__main__':
    main()