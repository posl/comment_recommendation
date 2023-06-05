def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算结果
    if a < 1 or a > 20 or b < 1 or b > 20:
        print(-1)
    else:
        print(a * b)

if __name__ == '__main__':
    main()