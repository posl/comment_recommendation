def distance(p1, p2):
    return sum([(a-b)**2 for a, b in zip(p1, p2)])**0.5
N, D = [int(x) for x in input().split()]
points = [[int(x) for x in input().split()] for _ in range(N)]
count = 0
for i in range(N):
    for j in range(i+1, N):
        if distance(points[i], points[j]).is_integer():
            count += 1
print(count)
