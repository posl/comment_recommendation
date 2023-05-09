def nCr(n,r):
    f=math.factorial
    return f(n) / f(r) / f(n-r)
import math
A,B,K = map(int, input().split())
ans = []
for i in range(A):
    ans.append('a')
for i in range(B):
    ans.append('b')
for i in range(A+B):
    if A == 0 or B == 0:
        break
    if K <= nCr(A+B-1,A-1):
        ans[A+B-1-i] = 'a'
        A -= 1
    else:
        K -= nCr(A+B-1,A-1)
        ans[A+B-1-i] = 'b'
        B -= 1
print(''.join(ans))
