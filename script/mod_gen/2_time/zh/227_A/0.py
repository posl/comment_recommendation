def get_distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)
N = int(input())
x = []
y = []
for i in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
dis = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        dis[i][j] = get_distance(x[i], y[i], x[j], y[j])
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            dis[j][k] = min(dis[j][k], dis[j][i] + dis[i][k])
ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        ans = max(ans, dis[i][j])
print(ans)

if __name__ == '__main__':
    get_distance()