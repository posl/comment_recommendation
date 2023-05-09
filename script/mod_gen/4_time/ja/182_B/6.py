def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(2, 1001):
    tmp = 0
    for j in a:
        if j % i == 0:
            tmp += 1
    if tmp > ans:
        ans = tmp
print(ans)

if __name__ == '__main__':
    gcd()