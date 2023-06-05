def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += N // i
    if N % i == 0:
        ans -= 1
print(ans)

if __name__ == '__main__':
    gcd()