def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        cnt = 0
        ball = [0]*N
        for j in range(K):
            if ((i >> j) & 1):
                ball[CD[j][0]-1] += 1
            else:
                ball[CD[j][1]-1] += 1
        for ab in AB:
            if ball[ab[0]-1] > 0 and ball[ab[1]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()