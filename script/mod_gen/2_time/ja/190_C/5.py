def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for i in range(K)]
    ans = 0
    for i in range(2**K):
        balls = [0]*N
        for j in range(K):
            if (i>>j)&1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        cnt = 0
        for k in range(M):
            if balls[AB[k][0]-1] > 0 and balls[AB[k][1]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
main()

if __name__ == '__main__':
    main()