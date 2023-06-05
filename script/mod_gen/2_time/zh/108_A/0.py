def get_median(x):
    x.sort()
    l = len(x)
    if l % 2 == 1:
        return x[l//2]
    else:
        return (x[l//2-1] + x[l//2]) // 2
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i, n):
        m.append(get_median(a[i:j+1]))
print(get_median(m))
