def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
N = int(input())
A = list(map(int,input().split()))
max_gcd = 0
for i in range(N):
    tmp_gcd = 0
    for j in range(N):
        if i == j:
            continue
        tmp_gcd = gcd(tmp_gcd, A[j])
    max_gcd = max(max_gcd, tmp_gcd)
print(max_gcd)

if __name__ == '__main__':
    gcd()