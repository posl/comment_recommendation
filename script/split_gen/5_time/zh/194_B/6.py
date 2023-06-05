def getMinTime(n, a, b):
    minTime = 0
    for i in range(n):
        minTime += min(a[i], b[i])
    return minTime
n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(getMinTime(n, a, b))
