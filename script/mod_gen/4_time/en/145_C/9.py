def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    # パスの長さ
    def path_len(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length
    # パスの総和
    def path_sum(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length
    # パスの平均
    def path_avg(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length / len(path)
    # パスの総和
    def path_sum(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length
    # パスの平均
    def path_avg(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length

if __name__ == '__main__':
    main()