def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N = int(input())
A = list(map(int, input().split()))
gcds = [0] * 1001
for a in A:
    for i in range(2, a + 1):
        if a % i == 0:
            gcds[i] += 1
print(gcds.index(max(gcds)))
