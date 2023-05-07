def get_center_and_height(n, points):
    for i in range(n):
        if points[i][2] != 0:
            break
    for cx in range(101):
        for cy in range(101):
            h = abs(cx - points[i][0]) + abs(cy - points[i][1]) + points[i][2]
            for j in range(n):
                if max(h - abs(cx - points[j][0]) - abs(cy - points[j][1]), 0) != points[j][2]:
                    break
            else:
                return cx, cy, h
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
print(*get_center_and_height(n, points))

if __name__ == '__main__':
    get_center_and_height()