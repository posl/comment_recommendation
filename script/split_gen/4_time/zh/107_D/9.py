def get_median(a):
    b = sorted(a)
    n = len(b)
    if n % 2 == 1:
        return b[n // 2]
    else:
        return b[n // 2 - 1]
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i, n):
        m.append(get_median(a[i:j + 1]))
print(get_median(m))
