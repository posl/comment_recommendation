def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
K = int(input())
n = 0
while K > 0:
    n += 1
    if n % S(n) == 0:
        K -= 1
print(n)
