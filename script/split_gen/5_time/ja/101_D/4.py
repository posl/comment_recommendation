def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
K = int(input())
n = 1
ans = []
while True:
    if S(n) * (n // S(n)) <= 10 ** 15:
        ans.append(S(n) * (n // S(n)))
    else:
        break
    n += 1
print(*sorted(ans)[:K], sep="\n")
