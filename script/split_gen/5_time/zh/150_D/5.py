def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
N,M = map(int,input().split())
A = list(map(int,input().split()))
A = list(set(A))
A.sort()
lcm = A[0]
for i in range(1,len(A)):
    lcm = lcm*A[i]//gcd(lcm,A[i])
count = 0
for i in range(1,M//lcm+1):
    if i%2==1:
        count += 1
        continue
    for j in range(len(A)):
        if i%A[j]==A[j]//2:
            count += 1
            break
print(count)
