def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
n = int(input())
x = []
y = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
ans = "No"
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1 = x[i] - x[j]
            y1 = y[i] - y[j]
            x2 = x[j] - x[k]
            y2 = y[j] - y[k]
            if x1*y2 == x2*y1:
                ans = "Yes"
                break
print(ans)

if __name__ == '__main__':
    gcd()