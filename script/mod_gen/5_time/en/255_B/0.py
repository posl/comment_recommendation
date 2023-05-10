def get_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]
distances = []
for i in range(n):
    for j in range(i + 1, n):
        distances.append(get_distance(xy[i][0], xy[i][1], xy[j][0], xy[j][1]))
distances.sort()
distances.reverse()
answer = 0
for i in range(k - 1):
    answer += distances[i]
print(answer)

if __name__ == '__main__':
    get_distance()