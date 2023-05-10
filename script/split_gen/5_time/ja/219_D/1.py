def main():
    # input
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # compute
    ans = float('inf')
    for i in range(2**N):
        cnt_t = 0
        cnt_y = 0
        cnt = 0
        for j in range(N):
            if (i >> j) & 1:
                cnt_t += AB[j][0]
                cnt_y += AB[j][1]
                cnt += 1
        if cnt_t >= X and cnt_y >= Y:
            ans = min(ans, cnt)
    # output
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
