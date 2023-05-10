def calc(a,b):
    return abs(a-b)
n = int(input())
a = list(map(int,input().split()))
a.sort()
b = a[n//2]
ans = 0
for i in range(n):
    ans += calc(a[i],b)
print(ans)
