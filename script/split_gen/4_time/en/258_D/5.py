def main():
    # input
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # compute
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
    ans += X * min([AB[i][1] for i in range(N)])
    # output
    print(ans)
