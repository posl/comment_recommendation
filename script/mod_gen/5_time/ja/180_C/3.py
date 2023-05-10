def get_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
        i += 1
    divisors.sort()
    return divisors
n = int(input())
divisors = get_divisors(n)
for i in divisors:
    print(i)

if __name__ == '__main__':
    get_divisors()