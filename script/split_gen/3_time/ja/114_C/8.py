def is753(n):
    if n < 100:
        return False
    if n < 1000:
        return n % 10 in [3, 5, 7] and n % 100 // 10 in [3, 5, 7] and n // 100 in [3, 5, 7]
    return is753(n % 10) and is753(n // 10)
n = int(input())
ans = 0
for i in range(357, n + 1):
    if is753(i):
        ans += 1
print(ans)
