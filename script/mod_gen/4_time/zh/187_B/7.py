def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n = int(input())
x = []
y = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        dx = x[i]-x[j]
        dy = y[i]-y[j]
        if dx<0:
            dx = -dx
            dy = -dy
        if dx==0:
            dy = abs(dy)
        else:
            g = gcd(dx,dy)
            dx = dx//g
            dy = dy//g
        if dx>=-dy and dx<=dy:
            ans += 1
print(ans)

if __name__ == '__main__':
    gcd()