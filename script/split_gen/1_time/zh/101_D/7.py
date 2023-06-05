def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
K = int(input())
i = 1
while K > 0:
    if i % S(i) == 0:
        print(i)
        K -= 1
    i += 1
