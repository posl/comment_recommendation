def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
    
ans = 0
for i in range(n):
    for j in range(i+1, n):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        if dx == 0:
            ans += 1
        else:
            if dy == 0:
                ans += 1
            else:
                if dx * dy > 0:
                    ans += 1
                else:
                    if abs(dx) >= abs(dy):
                        ans += 1
print(ans)
