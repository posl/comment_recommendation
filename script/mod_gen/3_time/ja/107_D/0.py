def median(a):
    a.sort()
    if len(a) % 2 == 1:
        return a[len(a) // 2]
    else:
        return (a[len(a) // 2 - 1] + a[len(a) // 2]) // 2
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i, n):
        m.append(median(a[i:j + 1]))
print(median(m))
