def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
n = int(input())
x = []
y = []
for _ in range(n):
    x1,y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        d = get_distance(x[i],y[i],x[j],y[j])
        if d > ans:
            ans = d
print(ans)

if __name__ == '__main__':
    get_distance()