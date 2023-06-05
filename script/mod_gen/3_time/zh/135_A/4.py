def main():
    # 读取输入
    a, b = map(int, input().split())
    # 处理
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()