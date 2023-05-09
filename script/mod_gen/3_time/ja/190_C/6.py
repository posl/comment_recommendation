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
        ball = [0]*N
        for j in range(K):
            if ((i>>j)&1):
                ball[CD[j][0]-1] += 1
            else:
                ball[CD[j][1]-1] += 1
        tmp = 0
        for j in range(M):
            if ball[AB[j][0]-1] > 0 and ball[AB[j][1]-1] > 0:
                tmp += 1
        ans = max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()