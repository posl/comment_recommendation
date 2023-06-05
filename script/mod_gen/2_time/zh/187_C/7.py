def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        x = xy[i][0] - xy[j][0]
        y = xy[i][1] - xy[j][1]
        if x == 0:
            ans += 1
        else:
            if x < 0:
                x *= -1
                y *= -1
            g = gcd(x, y)
            x //= g
            y //= g
            if -1 <= y <= 1:
                ans += 1
print(ans)

if __name__ == '__main__':
    gcd()