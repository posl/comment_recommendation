def get_divisors(n):
    """nの約数を全て求める"""
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors
n = int(input())
divisors = get_divisors(n)
ans = 0
for i in divisors:
    if i == 1:
        continue
    if (n - i) % i == 0:
        ans += (n - i) // i
print(ans)
