def S(n):
    return sum(int(i) for i in str(n))
K = int(input())
ans = []
n = 1
while len(ans) < K:
    if n / S(n) <= (n+1) / S(n+1):
        ans.append(n)
    n += 1
for i in ans:
    print(i)
