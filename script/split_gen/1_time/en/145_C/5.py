def solve():
    import itertools
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for p in itertools.permutations(range(n)):
        for i in range(n-1):
            ans += ((xy[p[i]][0]-xy[p[i+1]][0])**2+(xy[p[i]][1]-xy[p[i+1]][1])**2)**0.5
    print(ans/itertools.permutations(range(n)))
    
solve()
from itertools import permutations
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for p in permutations(range(n)):
    for i in range(n-1):
        ans += ((xy[p[i]][0]-xy[p[i+1]][0])**2+(xy[p[i]][1]-xy[p[i+1]][1])**2)**0.5
print(ans/len(list(permutations(range(n)))))
from itertools import permutations
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for p in permutations(range(n)):
    for i in range(n-1):
        ans += ((xy[p[i]][0]-xy[p[i+1]][0])**2+(xy[p[i]][1]-xy[p[i+1]][1])**2)**0.5
print(ans/len(list(permutations(range(n)))))
from itertools import permutations
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for p in permutations(range(n)):
    for i in range(n-1):
        ans += ((xy[p[i]][0]-xy[p[i+1]][0])**2+(xy[p[i]][1]-xy[p[i+1]][1])**2)**0.5
print(ans/len(list(permutations(range(n)))))
from itertools import permutations
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for p in permutations(range(n)):
    for i in range(n-1):
        ans += ((xy[p[i]][0]-xy[p[i+1]][0])**2+(xy[p[i]][1]-xy[p[i+1]][1])**2)**0.5
print(ans/len(list(per
