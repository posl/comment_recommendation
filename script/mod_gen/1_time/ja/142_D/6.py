def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
a, b = map(int, input().split())
d = gcd(a, b)
ans = 1
for i in range(2, int(d**0.5)+1):
    if d % i == 0:
        ans += 1
        if i != d // i:
            ans += 1
print(ans)

if __name__ == '__main__':
    gcd()