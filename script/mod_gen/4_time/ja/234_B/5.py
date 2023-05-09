def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
n = int(input())
l = []
for i in range(n):
    x,y = map(int,input().split())
    l.append((x,y))
ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans = max(ans,dist(l[i][0],l[i][1],l[j][0],l[j][1]))
print(ans)

if __name__ == '__main__':
    dist()