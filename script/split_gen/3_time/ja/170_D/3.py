def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
N = int(input())
A = list(map(int,input().split()))
L = [0]*(10**6+1)
for i in range(N):
    L[A[i]] += 1
for i in range(2,10**6+1):
    c = 0
    for j in range(i,10**6+1,i):
        c += L[j]
    if c > 1:
        break
else:
    print(0)
    exit()
for i in range(i,0,-1):
    c = 0
    for j in range(i,10**6+1,i):
        c += L[j]
    if c > 1:
        break
print(i)
