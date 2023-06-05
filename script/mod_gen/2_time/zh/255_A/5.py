def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
N = int(input())
ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if gcd(i, j) == 1:
            ans += 1
print(ans * 2)

if __name__ == '__main__':
    gcd()