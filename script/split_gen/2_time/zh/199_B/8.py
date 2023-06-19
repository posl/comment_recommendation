def count(x, a, b):
    count = 0
    for i in range(len(a)):
        if a[i] <= x <= b[i]:
            count += 1
    return count
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for x in range(1, 1001):
    if count(x, a, b) == n:
        ans += 1
print(ans)
