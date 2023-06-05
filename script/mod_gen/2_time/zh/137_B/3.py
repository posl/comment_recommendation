def main():
    # 读取标准输入
    a, b = map(int, input().split())
    # 计算
    print(max(a + b, a - b, a * b))

if __name__ == '__main__':
    main()