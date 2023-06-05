def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n//i)
    return divisors
N = int(input())
ans = 0
for i in range(1, N):
    ans += len(get_divisors(N-i))-1
print(ans)

if __name__ == '__main__':
    get_divisors()