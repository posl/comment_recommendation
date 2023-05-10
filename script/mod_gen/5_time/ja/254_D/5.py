def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
n = int(input())
ans = 0
for i in range(1, n+1):
    divs = get_divisors(i)
    for div in divs:
        if div**2 <= i:
            ans += 1
print(ans)

if __name__ == '__main__':
    get_divisors()