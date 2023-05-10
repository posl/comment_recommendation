def f(x):
    divisors = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            divisors += 2
    return divisors
N = int(input())
ans = 0
for i in range(1, N+1):
    ans += i * f(i)
print(ans)
