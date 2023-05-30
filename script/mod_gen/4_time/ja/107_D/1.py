def median(a):
    a = sorted(a)
    if len(a) % 2 == 1:
        return a[len(a) // 2]
    else:
        return (a[len(a) // 2] + a[len(a) // 2 - 1]) // 2
n = int(input())
a = [int(i) for i in input().split()]
m = []
for l in range(n):
    for r in range(l, n):
        m.append(median(a[l:r + 1]))
print(median(m))
