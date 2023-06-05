def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
A, B, K = map(int, input().split())
gcd = gcd(A, B)
ans = []
for i in range(1, gcd + 1):
    if gcd % i == 0:
        ans.append(i)
print(ans[-K])

if __name__ == '__main__':
    gcd()