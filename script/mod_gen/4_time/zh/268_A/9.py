def main():
    # 读取输入
    a, b, c, d, e = map(int, input().split())
    # 用集合去重
    print(len(set([a, b, c, d, e])))

if __name__ == '__main__':
    main()