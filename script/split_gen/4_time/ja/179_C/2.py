def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            divisors.append(i)
            if num//i != i:
                divisors.append(num//i)
    return divisors
N = int(input())
divisors = get_divisors(N)
ans = 0
for i in divisors:
    if i == 1:
        continue
    if (N - i) % i == 0:
        ans += (N - i) // i
print(ans)
