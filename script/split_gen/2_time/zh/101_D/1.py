def s(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
K = int(input())
n = 1
while K > 0:
    if s(n) * n <= K:
        K -= s(n)
    else:
        n += 1
print(n)
