def S(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum
K = int(input())
i = 0
n = 1
while i < K:
    if n % S(n) == 0:
        print(n)
        i += 1
    n += 1
