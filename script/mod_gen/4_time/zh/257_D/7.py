def main():
    N = int(input())
    pos = []
    for i in range(N):
        x, y, p = map(int, input().split())
        pos.append([x, y, p])
    # print(pos)
    # 计算两点之间的距离
    def distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    # 计算两点之间的距离是否可以跳跃
    def can_jump(x1, y1, p1, x2, y2):
        return p1 >= distance(x1, y1, x2, y2)
    # 计算两点之间的距离是否可以跳跃
    def can_jump2(x1, y1, p1, x2, y2, p2):
        return p1 * p2 >= distance(x1, y1, x2, y2)
    # 计算两点之间的距离是否可以跳跃
    def can_jump3(x1, y1, p1, x2, y2, p2):
        return p1 * p2 >= distance(x1, y1, x2, y2) * distance(x1, y1, x2, y2)
    # 计算两点之间的距离是否可以跳跃
    def can_jump4(x1, y1, p1, x2, y2, p2):
        return p1 * p2 * p2 >= distance(x1, y1, x2, y2) * distance(x1, y1, x2, y2)
    # 计算两点之间的距离是否可以跳跃
    def can_jump5(x1, y1, p1, x2, y2, p2):
        return p1 * p2 * p2 >= distance(x1, y1, x2, y2) * distance(x1, y1, x2, y2) * distance(x1, y1, x2, y2)
    # 计算两点之间的距离是否可以跳跃
    def can_jump

if __name__ == '__main__':
    main()