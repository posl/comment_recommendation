def median(a):
    a.sort()
    return a[len(a) // 2]
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += median(a[:i+1]) * (i + 1) - median(a[:i]) * i
print(ans)
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += median(a[i:]) * (i + 1) - median(a[i+1:]) * i
print(ans)
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += median(a[:i+1]) * (i + 1) - median(a[:i]) * i
    ans += median(a[i:]) * (i + 1) - median(a[i+1:]) * i
print(ans)
