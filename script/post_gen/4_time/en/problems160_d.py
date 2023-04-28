Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x, y = map(int, input().split())
    ans = [0] * n
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            ans[min(j - i, abs(x - i) + 1 + abs(y - j))] += 1
    print(*ans[1:], sep='\n')

=======
Suggestion 2

def solve():
    N, X, Y = map(int, input().split())
    ans = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(i - X) + 1 + abs(j - Y), abs(j - X) + 1 + abs(i - Y))
            ans[d] += 1
    for k in range(1, N):
        print(ans[k])

=======
Suggestion 3

def floyd_warshall(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

n, x, y = map(int, input().split())
x -= 1
y -= 1

d = [[n] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(n - 1):
    d[i][i + 1] = 1
    d[i + 1][i] = 1
d[x][y] = 1
d[y][x] = 1

d = floyd_warshall(d, n)

ans = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        ans[d[i][j]] += 1

print(*ans[1:], sep='\n')

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    result = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j))
            result[d - 1] += 1
    for i in range(N - 1):
        print(result[i])

=======
Suggestion 5

def solve():
    N, X, Y = map(int, input().split())
    ans = [0] * N
    for i in range(1, N):
        for j in range(i+1, N+1):
            d = min(j - i, abs(X - i) + abs(Y - j) + 1)
            ans[d] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 6

def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1

    ans = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            d = min(j-i, abs(x-i)+abs(y-j)+1)
            ans[d] += 1

    for i in range(1, n):
        print(ans[i])

=======
Suggestion 7

def main():
    N, X, Y = map(int, input().split())
    dist = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j))
            dist[d] += 1
    for k in range(1, N):
        print(dist[k])

=======
Suggestion 8

def main():
    n,x,y = map(int, input().split())
    ans = [0]*(n-1)
    for i in range(1,n):
        for j in range(i+1,n+1):
            tmp = min(j-i,abs(x-i)+1+abs(y-j),abs(y-i)+1+abs(x-j))
            ans[tmp-1] += 1
    for i in range(n-1):
        print(ans[i])

=======
Suggestion 9

def calc_dist(n, x, y):
    dist = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            dist[min(abs(i - j), abs(i - x) + 1 + abs(j - y), abs(i - y) + 1 + abs(j - x))] += 1
    return dist[1:]

=======
Suggestion 10

def get_input():
    return list(map(int, input().split()))
