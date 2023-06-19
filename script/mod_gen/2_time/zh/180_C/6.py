def get_divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors
N = int(input())
divisors = get_divisors(N)
for d in sorted(divisors):
    print(d)

if __name__ == '__main__':
    get_divisors()