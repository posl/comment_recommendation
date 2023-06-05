def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = list(map(int, input().split()))
        X.append(x)
        Y.append(y)
    # print(X)
    # print(Y)
    # 1. 两点之间的距离
    def distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    # 2. 两点之间的距离是否为偶数
    def is_even(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 2 == 0
    # 3. 两点之间的距离是否为奇数
    def is_odd(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 2 == 1
    # 4. 两点之间的距离是否为2的倍数
    def is_multiple_of_2(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 2 == 0
    # 5. 两点之间的距离是否为3的倍数
    def is_multiple_of_3(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 3 == 0
    # 6. 两点之间的距离是否为4的倍数
    def is_multiple_of_4(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 4 == 0
    # 7. 两点之间的距离是否为5的倍数
    def is_multiple_of_5(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 5 == 0
    # 8. 两点之间的距离是否为6的倍数
    def is_multiple

if __name__ == '__main__':
    main()