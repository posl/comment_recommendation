def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
n, m = map(int, input().split())
mod = 10**9 + 7
ans = 1
for x in divisors(m):
    if x < n:
        continue
    y = m // x
    if y < n:
        continue
    if y > x:
        continue
    if x == y:
        ans *= 1
    else:
        ans *= 2
    ans %= mod
print(ans)
