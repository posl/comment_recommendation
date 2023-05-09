Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    ans = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + abs(Y - j) + 1)
            ans[d] += 1
    for k in range(1, N):
        print(ans[k])

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    dist = [0] * (N - 1)
    for i in range(N):
        for j in range(i + 1, N):
            dist[min(j - i, abs(X - i) + 1 + abs(Y - j))] += 1
    for i in range(1, N):
        print(dist[i])

=======
Suggestion 3

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    ans = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j), abs(Y - i) + 1 + abs(X - j))
            ans[d] += 1
    print(*ans[1:], sep="\n")

=======
Suggestion 4

def solve():
    from collections import deque
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    ans = [0] * (n - 1)
    for i in range(n):
        for j in range(i + 1, n):
            d = min(j - i, abs(x - i) + 1 + abs(y - j))
            ans[d - 1] += 1
    print(*ans, sep='\n')

=======
Suggestion 5

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    ans = [0 for i in range(N-1)]
    for i in range(1, N):
        for j in range(i+1, N+1):
            d = min(abs(i-j), abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))
            ans[d-1] += 1
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 6

def main():
    N,X,Y = map(int,input().split())
    N = N + 1
    X = X - 1
    Y = Y - 1
    ans = [0 for i in range(N)]
    for i in range(N-1):
        for j in range(i+1,N):
            dist = min(j-i,abs(X-i)+1+abs(Y-j),abs(Y-i)+1+abs(X-j))
            ans[dist] = ans[dist] + 1

    for i in range(1,N):
        print(ans[i])

=======
Suggestion 7

def main():
    n,x,y = map(int,input().split())
    n = n - 1
    x = x - 1
    y = y - 1
    result = {}
    for i in range(n):
        for j in range(i+1,n+1):
            if i <= x and j <= x:
                result[j-i] = result.get(j-i,0) + 1
            elif i <= x and j > x and j <= y:
                result[min(j-i,i+1+x-j)] = result.get(min(j-i,i+1+x-j),0) + 1
            elif i <= x and j > y:
                result[min(j-i,i+1+x-y+y-j)] = result.get(min(j-i,i+1+x-y+y-j),0) + 1
            elif i > x and i <= y and j <= y:
                result[j-i] = result.get(j-i,0) + 1
            elif i > x and i <= y and j > y:
                result[min(j-i,i+1+y-j)] = result.get(min(j-i,i+1+y-j),0) + 1
            elif i > y and j > y:
                result[j-i] = result.get(j-i,0) + 1
    for i in range(1,n):
        print(result.get(i,0))

=======
Suggestion 8

def main():
    #import sys
    #f = open('test.txt', 'r')
    #sys.stdin = f

    N, X, Y = map(int, input().split())

    ans = [0] * (N-1)
    for i in range(1, N):
        for j in range(i+1, N+1):
            if j - i <= X:
                ans[j-i-1] += 1
            elif i <= X and j > X and j - i <= Y:
                ans[min(j-X-1, i-1+Y-X)] += 1
            elif i > X and j > X and j - i <= Y:
                ans[min(j-i-1, i-X-1+Y-X)] += 1
            else:
                ans[min(j-i-1, i-X-1+Y-X)] += 1
                ans[min(j-i-1, i-1+Y-X)] += 1
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 9

def solve():
    N, X, Y = map(int, input().split())
    N -= 1
    X -= 1
    Y -= 1

    def solve_(k):
        d = [0] * N
        for i in range(N):
            for j in range(i+1, N):
                d[min(j-i, abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))] += 1
        return d[k]

    for k in range(1, N):
        print(solve_(k))

=======
Suggestion 10

def main():
    n,x,y = map(int,input().split())
    #print(n,x,y)
    #print('Hello World!')
    dist = [0] * (n)
    for i in range(1,n):
        for j in range(i+1,n+1):
            dist[min(abs(i-j),abs(x-i)+1+abs(y-j),abs(y-i)+1+abs(x-j))] += 1
    for i in range(1,n):
        print(dist[i])
    return 0
