def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())
import itertools
l = list(itertools.permutations(range(n)))
ans = 0
for i in range(len(l)):
    for j in range(n-1):
        ans += dist(x[l[i][j]],y[l[i][j]],x[l[i][j+1]],y[l[i][j+1]])
print(ans/len(l))

if __name__ == '__main__':
    dist()