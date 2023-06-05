def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if abs(points[i][0] - points[j][0]) <= abs(points[i][1] - points[j][1]):
            cnt += 1
print(cnt)

if __name__ == '__main__':
    gcd()