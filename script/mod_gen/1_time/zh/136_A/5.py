def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 从2号瓶中尽可能地将水转移到1号瓶
    # 2号瓶中剩余水量
    C -= A - B
    # 输出结果
    print(C if C >= 0 else 0)

if __name__ == '__main__':
    main()