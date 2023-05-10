def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = [0] * (m + 1)
for i in range(n):
    for j in range(a[i], m + 1, a[i]):
        b[j] = 1
ans = []
for i in range(1, m + 1):
    if b[i] == 0:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)

if __name__ == '__main__':
    gcd()