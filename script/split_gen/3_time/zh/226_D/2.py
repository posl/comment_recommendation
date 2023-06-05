def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
towns = []
for i in range(n):
    x, y = map(int, input().split())
    towns.append((x, y))
towns.sort()
towns = tuple(towns)
dict = {}
for i in range(n):
    for j in range(i+1, n):
        x = towns[j][0] - towns[i][0]
        y = towns[j][1] - towns[i][1]
        if x < 0:
            x, y = -x, -y
        if x == 0:
            y = 1
        elif y == 0:
            x = 1
        else:
            g = gcd(x, y)
            x //= g
            y //= g
        if (x, y) in dict:
            dict[(x, y)] += 1
        else:
            dict[(x, y)] = 1
ans = n
for k, v in dict.items():
    ans = min(ans, n - v)
print(ans)
