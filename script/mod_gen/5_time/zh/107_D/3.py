def median(a):
    if len(a) % 2 == 0:
        return (a[len(a)/2-1] + a[len(a)/2])/2
    else:
        return a[len(a)/2]
n = int(raw_input())
a = map(int, raw_input().split())
b = []
for i in range(n):
    b.append(a[i])
    print median(sorted(b))
