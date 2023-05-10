def count_divisor(n):
    count = 0
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            n //= i
            count += 1
    if n != 1:
        count += 1
    return count
n = int(input())
ans = 0
divisors = [0 for _ in range(n+1)]
for i in range(2, n+1):
    divisors[i] = count_divisor(i)
for i in range(2, n+1):
    if divisors[i] >= 74:
        ans += 1
for i in range(2, n+1):
    for j in range(i+1, n+1):
        if divisors[i] >= 2 and divisors[j] >= 24:
            ans += 1
        if divisors[i] >= 4 and divisors[j] >= 14:
            ans += 1
        if divisors[i] >= 14 and divisors[j] >= 4:
            ans += 1
        if divisors[i] >= 24 and divisors[j] >= 2:
            ans += 1
print(ans)

if __name__ == '__main__':
    count_divisor()