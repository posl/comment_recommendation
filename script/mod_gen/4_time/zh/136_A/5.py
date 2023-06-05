def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 从2号瓶中转移水
    C -= A - B
    # 答案
    print(C if C >= 0 else 0)

if __name__ == '__main__':
    main()