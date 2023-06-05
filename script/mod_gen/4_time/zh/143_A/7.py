def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算并输出结果
    print(max(0, A - B * 2))

if __name__ == '__main__':
    main()