def solve():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    points = list(map(list, zip(*points)))
    points[0] = [points[0][0]] + [0] + points[0]
    points[1] = [0] + [points[1][0]] + points[1

if __name__ == '__main__':
    solve()