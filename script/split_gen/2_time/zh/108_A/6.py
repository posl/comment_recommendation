def get_median(a):
    a.sort()
    return a[len(a)//2]
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i, n):
        m.append(get_median(a[i:j+1]))
print(get_median(m))
