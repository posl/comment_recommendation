def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    slopes = {}
    for j in range(n):
        if i == j:
            continue
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        if dx == 0:
            slope = float('inf')
        else:
            slope = dy / dx
        if slope not in slopes:
            slopes[slope] = 0
        slopes[slope] += 1
    for slope in slopes:
        ans += slopes[slope] * (slopes[slope] - 1) // 2
print(ans // 2)

if __name__ == '__main__':
    gcd()