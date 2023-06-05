def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum
K = int(input())
count = 0
n = 1
while count < K:
    if n % S(n) == 0:
        print(n)
        count += 1
    n += 1
