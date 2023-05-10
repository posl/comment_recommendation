def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
GCD = [0] * (A[0]+1)
for i in range(N):
    for j in range(2, A[i]+1):
        if A[i] % j == 0:
            GCD[j] += 1
print(GCD.index(max(GCD)))
