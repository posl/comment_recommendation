Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x, y = map(int, input().split())
    ans = [0] * (n - 1)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            ans[min(j - i, abs(x - i) + 1 + abs(y - j))] += 1
    for i in range(1, n):
        print(ans[i])

main()

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    ans = [0] * (N-1)
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            dist = min(j-i, abs(X-i) + 1 + abs(j-Y))
            ans[dist-1] += 1
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    ans = [0] * (N-1)
    for i in range(1, N):
        for j in range(i+1, N+1):
            d = min(j-i, abs(X-i)+1+abs(Y-j))
            ans[d-1] += 1
    for a in ans:
        print(a)

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    ans = [0] * N
    for i in range(1, N):
        for j in range(i+1, N+1):
            d = min(j-i, abs(X-i)+1+abs(Y-j))
            ans[d] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 5

def main():
    N, X, Y = map(int, input().split())
    ans = [0 for i in range(N-1)]
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            d = min(j-i, abs(X-i)+1+abs(Y-j))
            ans[d-1] += 1
    for a in ans:
        print(a)

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    count = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            count[min(j-i, abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))] += 1
    for i in range(1, N):
        print(count[i])

=======
Suggestion 7

def solve():
    N, X, Y = map(int, input().split())
    dist = [0 for _ in range(N)]
    for i in range(1, N):
        for j in range(i+1, N+1):
            if i <= X <= j or i <= Y <= j:
                dist[min(j-i, abs(X-i)+1+abs(Y-j))] += 1
            else:
                dist[j-i] += 1
    for i in range(1, N):
        print(dist[i])

solve()

=======
Suggestion 8

def main():
    N, X, Y = map(int, input().split())
    G = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i == j:
                continue
            elif j == X:
                G[i][j] = 1
                G[j][i] = 1
            elif j == Y:
                G[i][j] = 1
                G[j][i] = 1
            elif j == i+1:
                G[i][j] = 1
                G[j][i] = 1
            else:
                G[i][j] = 1000
                G[j][i] = 1000
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]
    ans = [0]*(N-1)
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if G[i][j] != 1000:
                ans[G[i][j]-1] += 1
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 9

def main():
    N, X, Y = list(map(int, input().split()))
    distance = [0] * N
    for i in range(1, N):
        for j in range(i+1, N+1):
            d = min(j-i, abs(X-i)+1+abs(Y-j))
            distance[d] += 1
    for i in range(1, N):
        print(distance[i])

=======
Suggestion 10

def solve():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    ans = [0] * (N - 1)
    for i in range(N):
        for j in range(i + 1, N):
            dist = min(j - i, abs(X - i) + 1 + abs(j - Y))
            ans[dist - 1] += 1
    print(*ans, sep='

')
