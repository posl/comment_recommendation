def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
A.sort()
A.reverse()
# print(A)
B = [0] * N
B[0] = A[0]
for i in range(1, N):
    B[i] = gcd(B[i-1], A[i])
# print(B)
print(B[N-1])
