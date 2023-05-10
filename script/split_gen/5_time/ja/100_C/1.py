def check(n):
    if n % 2 == 0:
        return 1 + check(n/2)
    else:
        return 0
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += check(i)
print(ans)
