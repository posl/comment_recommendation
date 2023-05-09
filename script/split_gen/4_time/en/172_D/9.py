def get_divisors(x):
    divisors = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            divisors += 1
            if x // i != i:
                divisors += 1
    return divisors
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * get_divisors(i)
print(ans)
