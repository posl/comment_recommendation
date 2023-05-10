def calc_sum(a, b):
    return (a + b) * (b - a + 1) // 2
n = int(input())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += calc_sum(a, b)
print(ans)
