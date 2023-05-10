def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num//i)
    return divisors
n = int(input())
ans = 0
for i in range(1, n+1):
    divisors = get_divisors(i)
    ans += i * len(divisors)
print(ans)

if __name__ == '__main__':
    get_divisors()