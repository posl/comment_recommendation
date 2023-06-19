def main():
    # 读入
    a_1, a_2, a_3 = map(int, input().split())
    # 逻辑处理
    # 1. a_1, a_2, a_3中有两个数相等
    if a_1 == a_2 or a_1 == a_3 or a_2 == a_3:
        ans = 0
    # 2. a_1, a_2, a_3中的三个数不相等
    else:
        ans = min(abs(a_1 - a_2) + abs(a_1 - a_3), abs(a_2 - a_1) + abs(a_2 - a_3), abs(a_3 - a_1) + abs(a_3 - a_2))
    # 输出
    print(ans)

if __name__ == '__main__':
    main()