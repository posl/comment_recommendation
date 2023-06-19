def main():
    # 读入
    a, b, c = map(int, input().split())
    # 处理
    print(a + b + c - min(a, b, c))

if __name__ == '__main__':
    main()