def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a
n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if gcd(a[i], a[j]) == a[k] or gcd(a[j], a[k]) == a[i] or gcd(a[k], a[i]) == a[j]:
                cnt += 1
print(cnt)

if __name__ == '__main__':
    gcd()