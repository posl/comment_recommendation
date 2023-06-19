def main():
    # 读入S和T
    s, t = input().split()
    # 读入A和B
    a, b = map(int, input().split())
    # 读入U
    u = input()
    # 计算答案并打印
    if u == s:
        print(a - 1, b)
    elif u == t:
        print(a, b - 1)

if __name__ == '__main__':
    main()