def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        balls = [False] * N
        for j in range(K):
            if i >> j & 1:
                balls[CD[j][0] - 1] = True
            else:
                balls[CD[j][1] - 1] = True
        cnt = 0
        for j in range(M):
            if balls[AB[j][0] - 1] and balls[AB[j][1] - 1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()