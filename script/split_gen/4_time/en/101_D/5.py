def S(n):
    return sum(int(i) for i in str(n))
K = int(input())
n = 1
ans = []
while len(ans) < K:
    if n / S(n) <= (n+1) / S(n+1):
        ans.append(n)
    n += 1
print(*ans, sep='\n')
