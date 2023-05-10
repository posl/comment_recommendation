def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = set()
for a in A:
    for i in range(1, M//a + 1):
        S.add(a*i)
ans = []
for i in range(1, M+1):
    if i not in S:
        ans.append(i)
print(len(ans))
for a in ans:
    print(a)
