def get_input():
    points = []
    for i in range(4):
        points.append(list(map(int, input().split())))
    return points

if __name__ == '__main__':
    get_input()