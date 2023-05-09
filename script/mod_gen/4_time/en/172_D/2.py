def f(x):
    divisors = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            divisors += 1
            if x // i != i:
                divisors += 1
    return divisors
n = int(input())
ans = 0
for k in range(1, n+1):
    ans += k * f(k)
print(ans)

if __name__ == '__main__':
    f()