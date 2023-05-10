def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy.sort()
xy = [[xy[i][0]-xy[0][0], xy[i][1]-xy[0][1]] for i in range(n)]
ans = 10**9
for i in range(n):
    for j in range(i+1, n):
        x = xy[i][0]-xy[j][0]
        y = xy[i][1]-xy[j][1]
        ans = min(ans, gcd(x,y))
print(ans)

if __name__ == '__main__':
    gcd()