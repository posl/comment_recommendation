def get_divisor(n):
    i = 2
    divisors = []
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        divisors.append(n)
    return divisors
n = int(input())
divisors = get_divisor(n)
divisors_set = set(divisors)
ans = 0
for d in divisors_set:
    if divisors.count(d) >= 4:
        ans += 1
    if divisors.count(d) >= 2:
        for d2 in divisors_set:
            if d == d2:
                continue
            if divisors.count(d2) >= 2:
                ans += 1
print(ans)
