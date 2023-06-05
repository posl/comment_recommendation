def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
K = int(input())
snuke = []
n = 1
while len(snuke) < K:
    if n % S(n) == 0:
        snuke.append(n)
    n += 1
for i in range(K):
    print(snuke[i])
