def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n - 1):
    if a[i] == a[i + 1]:
        ans += 1
    else:
        for j in range(i + 1, n):
            if a[j] == a[i]:
                ans += 1
            elif a[j] % a[i] == 0:
                break
print(ans)

if __name__ == '__main__':
    gcd()