def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
N,M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A_gcd = A[0]
for i in range(1,N):
    A_gcd = gcd(A_gcd, A[i])
ans = []
for i in range(1,M+1):
    if gcd(A_gcd, i) == 1:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)

if __name__ == '__main__':
    gcd()