def findMedian(a):
    a.sort()
    n = len(a)
    if n % 2 == 1:
        return a[n // 2]
    else:
        return a[n // 2 - 1]
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i, n):
        m.append(findMedian(a[i:j + 1]))
print(findMedian(m))
