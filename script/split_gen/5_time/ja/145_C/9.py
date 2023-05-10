def main():
    N = int(input())
    xy = []
    for i in range(N):
        x,y = map(int,input().split())
        xy.append([x,y])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += ((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**(1/2)
    ans /= N
    print(ans)
