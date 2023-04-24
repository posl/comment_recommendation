Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    dist = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j))
            dist[d] += 1
    for i in range(1, N):
        print(dist[i])

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    dist = [0] * (N - 1)
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            dist[min(j - i, abs(X - i) + abs(Y - j) + 1) - 1] += 1
    for i in range(N - 1):
        print(dist[i])

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    for k in range(1, N):
        ans = 0
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                if abs(i - j) == k:
                    ans += 1
                elif abs(i - X) + 1 + abs(Y - j) == k:
                    ans += 1
                elif abs(i - Y) + 1 + abs(X - j) == k:
                    ans += 1
        print(ans)

=======
Suggestion 4

def solve():
    N, X, Y = map(int, input().split())
    ans = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j))
            ans[d] += 1
    for i in range(1, N):
        print(ans[i])

solve()

=======
Suggestion 5

def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    ans = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            ans[min(j-i, abs(i-x)+1+abs(j-y))] += 1
    for i in range(1, n):
        print(ans[i])

=======
Suggestion 6

def solve():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    ans = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            dist = min(j - i, abs(X - i) + 1 + abs(Y - j))
            ans[dist] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 7

def solve(n, x, y):
    ans = [0] * n
    for i in range(1, n):
        for j in range(i+1, n+1):
            ans[min(j-i, abs(x-i)+1+abs(y-j), abs(y-i)+1+abs(x-j))-1] += 1
    return ans

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    dist = [0] * (N-1)
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            dist[min(j-i, abs(X-i)+1+abs(j-Y))] += 1
    for i in range(1, N):
        print(dist[i])
