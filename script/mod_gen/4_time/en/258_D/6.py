def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        if ans > X * AB[i][1]:
            ans = X * AB[i][1]
        X -= 1
        if X == 0:
            break
    print(ans)

if __name__ == '__main__':
    solve()