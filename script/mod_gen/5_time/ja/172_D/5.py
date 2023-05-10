def divisors(n):
    divisors = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return divisors
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * len(divisors(i))
print(ans)

if __name__ == '__main__':
    divisors()