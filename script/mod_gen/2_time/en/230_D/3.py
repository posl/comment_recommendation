def solve():
    N, D = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if ans >= LR[i][1]:
            continue
        ans = LR[i][0] + D - 1
    print(ans)

if __name__ == '__main__':
    solve()