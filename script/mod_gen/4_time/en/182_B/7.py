def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
gcdness = [0] * (a[0] + 1)
for i in range(n):
    for j in range(2, a[i] + 1):
        if gcdness[j] == 1:
            continue
        if a[i] % j == 0:
            gcdness[j] += 1
            k = j + j
            while k <= a[0]:
                gcdness[k] = 1
                k += j
ans = 0
for i in range(2, a[0] + 1):
    if gcdness[i] > 1:
        ans = i
print(ans)

if __name__ == '__main__':
    gcd()