def main():
    N,M = map(int,input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int,input().split())))
    K = int(input())
    CD = []
    for i in range(K):
        CD.append(list(map(int,input().split())))
    ans = 0
    for i in range(2**K):
        cnt = 0
        balls = [0]*N
        for j in range(K):
            if (i>>j)&1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        for k in range(M):
            if balls[AB[k][0]-1] and balls[AB[k][1]-1]:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)
