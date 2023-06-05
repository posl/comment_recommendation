def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
count = 0
for i in range(N):
    for j in range(i+1, N):
        if abs(points[i][0] - points[j][0]) <= abs(points[i][1] - points[j][1]):
            count += 1
print(count)

if __name__ == '__main__':
    gcd()