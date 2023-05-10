def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0: 
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
N = int(input())
ans = 0
divisors = make_divisors(N)
divisors.sort(reverse=True)
for i in divisors:
    if i == 1:
        break
    n = N
    while n % i == 0:
        n = n // i
    if n % i == 1:
        ans += 1
print(ans)

if __name__ == '__main__':
    make_divisors()