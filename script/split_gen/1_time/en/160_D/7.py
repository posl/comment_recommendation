def solve():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    ans = [0 for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            dis = min(j-i, abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))
            ans[dis] += 1
    for i in range(1, N):
        print(ans[i])
