def get_input():
    n = int(raw_input())
    points = []
    for i in range(n):
        x, y = map(int, raw_input().split())
        points.append((x, y))
    return points

if __name__ == '__main__':
    get_input()