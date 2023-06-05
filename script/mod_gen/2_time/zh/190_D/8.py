def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for i in range(K)]
    ans = 0
    for i in range(2**K):
        bits = [0]*K
        for j in range(K):
            if ((i>>j) & 1):
                bits[j] = 1
        balls = [0] * N
        for j in range(K):
            if bits[j] == 0:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        cnt = 0
        for j in range(M):
            if balls[AB[j][0]-1] >= 1 and balls[AB[j][1]-1] >= 1:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

if __name__ == '__main__':
    main()