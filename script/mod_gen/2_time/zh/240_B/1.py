def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    # 用集合存储不同的整数
    s = set()
    for x in a:
        s.add(x)
    # 打印答案
    print(len(s))

if __name__ == '__main__':
    main()