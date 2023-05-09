def f(m):
    sum = 0
    for i in range(N):
        sum += m % a[i]
    return sum
N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
l = 0
r = a[0] * (N - 1)
while r - l > 1:
    m = (l + r) // 2
    if f(m) >= f(m + 1):
        r = m
    else:
        l = m
print(f(r))
