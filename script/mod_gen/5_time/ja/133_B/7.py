def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k])**2
        if dist**0.5 == int(dist**0.5):
            ans += 1
print(ans)

if __name__ == '__main__':
    gcd()