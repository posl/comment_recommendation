def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        d = distance(points[i][0], points[i][1], points[j][0], points[j][1])
        if d > ans:
            ans = d
print(ans)

if __name__ == '__main__':
    distance()