def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
N = int(input())
count = 0
for i in range(1, N + 1, 2):
    if count_divisors(i) == 8:
        count += 1
print(count)

if __name__ == '__main__':
    count_divisors()