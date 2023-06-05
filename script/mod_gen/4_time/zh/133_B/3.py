def distance(x,y):
    d = 0
    for i in range(len(x)):
        d += (x[i]-y[i])**2
    return d**0.5
n,d = map(int,input().split())
x = []
for i in range(n):
    x.append(list(map(int,input().split())))
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        if distance(x[i],x[j])%1 == 0:
            ans += 1
print(ans)

if __name__ == '__main__':
    distance()