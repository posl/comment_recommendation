def solve():
    N,X = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
    ans += X * min([AB[i][1] for i in range(N)])
    print(ans)

if __name__ == '__main__':
    solve()