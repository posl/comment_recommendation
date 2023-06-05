def main():
    # 读取数据
    a, b, c = map(int, input().split())
    # 计算答案
    print(c - (a - b) if c - (a - b) >= 0 else c)

if __name__ == '__main__':
    main()