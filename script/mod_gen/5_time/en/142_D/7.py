def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a,b = map(int, input().split())
g = gcd(a,b)
cnt = 1
for i in range(2, int(g**0.5)+1):
    if g%i == 0:
        cnt += 1
        if i != g//i:
            cnt += 1
print(cnt)

if __name__ == '__main__':
    gcd()