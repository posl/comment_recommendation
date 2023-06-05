def get_input():
    n = int(raw_input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, raw_input().split())))
    return points

if __name__ == '__main__':
    get_input()