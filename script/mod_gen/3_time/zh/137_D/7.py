def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while M > 0:
        if i >= N:
            break
        if AB[i][0] > M:
            break
        ans += AB[i][1]
        M -= AB[i][0]
        i += 1
    print(ans)

if __name__ == '__main__':
    solve()