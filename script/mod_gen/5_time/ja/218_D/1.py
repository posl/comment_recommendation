def get_input():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return n, points

if __name__ == '__main__':
    get_input()