def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors
N = int(input())
divisors = get_divisors(N)
count = 0
for i in range(len(divisors)):
    for j in range(i, len(divisors)):
        if N % divisors[i] == 0 and N // divisors[i] % divisors[j] == 0:
            count += 1
print(count)

if __name__ == '__main__':
    get_divisors()