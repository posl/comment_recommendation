def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
gcd_max = 0
gcd_list = [0 for _ in range(N)]
gcd_list[0] = A[0]
gcd_list[N - 1] = A[N - 1]
for i in range(1, N):
    gcd_list[i] = gcd(gcd_list[i - 1], A[i])
gcd_max = max(gcd_max, gcd_list[N - 2])
for i in range(N - 1, 0, -1):
    gcd_list[i] = gcd(gcd_list[i + 1], A[i])
gcd_max = max(gcd_max, gcd_list[1])
for i in range(1, N - 1):
    gcd_max = max(gcd_max, gcd(gcd_list[i - 1], gcd_list[i + 1]))
print(gcd_max)
