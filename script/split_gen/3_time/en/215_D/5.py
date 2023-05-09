def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
N,M = map(int,input().split())
A = list(map(int,input().split()))
L = [0] * (M+1)
for i in range(N):
    for j in range(A[i], M+1, A[i]):
        L[j] = 1
ans = []
for i in range(1, M+1):
    if L[i] == 0:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)
