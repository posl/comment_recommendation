def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
A = list(set(A))
B = [0]*(M+1)
for i in range(len(A)):
    if A[i] == 1:
        continue
    if B[A[i]] == 1:
        continue
    else:
        B[A[i]] = 1
        for j in range(2,M//A[i]+1):
            B[A[i]*j] = 1
ans = []
for i in range(1,M+1):
    if B[i] == 0:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
