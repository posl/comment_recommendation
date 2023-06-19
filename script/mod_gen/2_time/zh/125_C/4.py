def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
N = input()
A = map(int,raw_input().split())
A.sort()
gcd_num = A[0]
for i in range(1,N):
    gcd_num = gcd(gcd_num,A[i])
print gcd_num
