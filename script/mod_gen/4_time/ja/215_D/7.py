def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
b = [0] * (m + 1)
for i in range(n):
    if b[a[i]] == 0:
        b[a[i]] = 1
        for j in range(a[i] * 2, m + 1, a[i]):
            b[j] = 2
for i in range(1, m + 1):
    if b[i] == 1:
        for j in range(i * 2, m + 1, i):
            b[j] = 2
ans = []
for i in range(1, m + 1):
    if b[i] == 1:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

if __name__ == '__main__':
    gcd()