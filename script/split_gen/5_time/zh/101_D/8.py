def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
K = int(input())
n = 0
i = 0
while i < K:
    n += 1
    if n % sum_digits(n) == 0:
        i += 1
        print(n)
