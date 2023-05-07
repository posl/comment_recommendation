def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N = int(input())
A = list(map(int, input().split()))
gcds = {}
for i in range(N):
    for j in range(i+1, N):
        g = gcd(A[i], A[j])
        if g in gcds:
            gcds[g] += 1
        else:
            gcds[g] = 1
max_gcd = 0
max_gcd_cnt = 0
for k, v in gcds.items():
    if v > max_gcd_cnt:
        max_gcd = k
        max_gcd_cnt = v
print(max_gcd)
