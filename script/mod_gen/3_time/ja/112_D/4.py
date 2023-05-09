def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N, M = map(int, input().split())
for i in range(1, int(M ** 0.5) + 1):
    if M % i == 0:
        j = M // i
        if i * N <= M:
            ans = i
        if j * N <= M:
            ans = j
print(ans)

if __name__ == '__main__':
    gcd()