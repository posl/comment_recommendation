def get_point():
    point = []
    for i in range(3):
        x, y = map(int, input().split())
        point.append([x, y])
    return point
