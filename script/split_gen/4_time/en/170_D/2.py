def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    if a[i] != a[i-1]:
        divisors = get_divisors(a[i])
        if len(divisors) == 2:
            ans += 1
        else:
            for j in range(1, len(divisors)):
                if divisors[j] == 1 or divisors[j] == a[i]:
                    continue
                if a[i] % divisors[j] == 0 and divisors[j] in a:
                    break
            else:
                ans += 1
print(ans)
