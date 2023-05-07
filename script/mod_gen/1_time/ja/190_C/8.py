def main():
    N,M = map(int,input().split())
    cond = []
    for i in range(M):
        cond.append(list(map(int,input().split())))
    K = int(input())
    ball = []
    for i in range(K):
        ball.append(list(map(int,input().split())))
    ans = 0
    for i in range(2**K):
        tmp = [0]*N
        for j in range(K):
            if (i>>j)&1:
                tmp[ball[j][1]-1] += 1
            else:
                tmp[ball[j][0]-1] += 1
        cnt = 0
        for j in range(M):
            if tmp[cond[j][0]-1] > 0 and tmp[cond[j][1]-1] > 0:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

if __name__ == '__main__':
    main()