def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
K = int(input())
ans = []
n = 1
while len(ans) < K:
    if n // S(n) > 1:
        ans.append(n)
    n += 1
for a in ans:
    print(a)

if __name__ == '__main__':
    S()