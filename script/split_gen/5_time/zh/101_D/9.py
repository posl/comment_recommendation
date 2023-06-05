def S(n):
    return sum(map(int, str(n)))
K = int(input())
N = 0
ans = []
while len(ans) < K:
    N += 1
    if N % S(N) == 0:
        ans.append(N)
for i in ans:
    print(i)
