def main():
    N,D = map(int,input().split())
    wall = [list(map(int,input().split())) for i in range(N)]
    wall.sort(key=lambda x:x[1])
    #print(wall)
    ans = 0
    for i in range(N):
        if wall[i][0] > D:
            wall[i][0] -= D
            wall[i][1] -= D
        else:
            wall[i][0] = 1
            wall[i][1] -= D
        if wall[i][0] <= 0:
            wall[i][0] = 1
    wall.sort(key=lambda x:x[0])
    #print(wall)
    for i in range(N):
        if wall[i][0] == 1:
            ans += 1
            for j in range(i+1,N):
                if wall[j][0] <= wall[i][1]:
                    wall[j][0] = wall[i][1] + 1
                else:
                    break
    print(ans)
