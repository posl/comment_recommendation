def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
N = int(input())
divisors = get_divisors(N)
ans = 0
for i in range(len(divisors)):
    for j in range(i, len(divisors)):
        if (divisors[i] * divisors[j]) <= N:
            ans += 1
print(ans)
