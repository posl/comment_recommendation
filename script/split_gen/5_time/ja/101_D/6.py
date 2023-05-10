def s(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s
K = int(input())
n = 1
while K > 0:
    if n % s(n) == 0:
        print(n)
        K -= 1
    n += 1
