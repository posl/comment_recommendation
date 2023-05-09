def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
max_a = A[-1]
max_gcd = 0
for a in A:
    if a == 1:
        continue
    if max_gcd == 1:
        break
    if a > max_gcd:
        max_gcd = a
    else:
        continue
    for i in range(2, a):
        if a % i == 0:
            continue
        if gcd(i, a) == 1:
            max_gcd = i
            break
        else:
            continue
