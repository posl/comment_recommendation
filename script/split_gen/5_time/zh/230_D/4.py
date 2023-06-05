def solve(n,d,wall):
    #wall = sorted(wall,key=lambda x:x[0])
    r = 0
    for i in range(n):
        if i == n-1:
            r += (wall[i][1] - wall[i][0] + d) // d
        else:
            r += (wall[i][1] - wall[i][0] + d) // d - 1
    return r
n,d = map(int,input().split())
wall = []
for i in range(n):
    l,r = map(int,input().split())
    wall.append([l,r])
print(solve(n,d,wall))
