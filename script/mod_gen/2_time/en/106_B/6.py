def count_divisors(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c
n = int(input())
c = 0
for i in range(1, n + 1, 2):
    if count_divisors(i) == 8:
        c += 1
print(c)

if __name__ == '__main__':
    count_divisors()