def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算并打印答案
    print(max(0, a - b * 2))

if __name__ == '__main__':
    main()