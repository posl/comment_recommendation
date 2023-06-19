def main():
    # 读取输入
    a, b, c, d = map(int, input().split())
    # 用来判断是否可以实现目标
    if a < b * d:
        print(-1)
        return
    # 用来判断需要多少次操作
    if c * d - b <= 0:
        print(-1)
        return
    # 计算答案
    print((a + c * d - b - 1) // (c * d - b))

if __name__ == '__main__':
    main()