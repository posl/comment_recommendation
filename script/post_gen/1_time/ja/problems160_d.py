Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x,y = map(int,input().split())
    ans = [0]*(n-1)
    for i in range(1,n):
        for j in range(i+1,n+1):
            k = min(j-i,abs(x-i)+1+abs(y-j))
            ans[k-1] += 1
    for i in ans:
        print(i)

=======
Suggestion 2

def main():
    N,X,Y = map(int,input().split())
    ans = [0] * N
    for i in range(1,N):
        for j in range(i+1,N+1):
            tmp = min(j-i,abs(i-X)+1+abs(j-Y))
            ans[tmp] += 1
    for i in range(1,N):
        print(ans[i])

=======
Suggestion 3

def main():
    N,X,Y = map(int,input().split())
    N -= 1
    X -= 1
    Y -= 1
    ans = [0]*N
    for i in range(N):
        for j in range(i+1,N):
            dist = min(j-i,abs(X-i)+1+abs(Y-j),abs(Y-i)+1+abs(X-j))
            ans[dist] += 1
    for i in range(1,N):
        print(ans[i])
main()

=======
Suggestion 4

def main():
    n,x,y = map(int,input().split())
    ans = [0] * n
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            k = min(j-i,abs(x-i)+1+abs(y-j))
            ans[k] += 1
    for i in range(1,n):
        print(ans[i])

=======
Suggestion 5

def main():
    n,x,y = map(int,input().split())
    ans = [0]*n
    for i in range(1,n):
        for j in range(i+1,n+1):
            ans[min(abs(i-j),abs(x-i)+1+abs(y-j))] += 1
    for i in range(1,n):
        print(ans[i])

=======
Suggestion 6

def main():
    n,x,y = map(int,input().split())
    ans = [0]*(n-1)
    for i in range(1,n):
        for j in range(i+1,n+1):
            #print(i,j)
            d = min(j-i,abs(x-i)+1+abs(y-j),abs(y-i)+1+abs(x-j))
            #print(d)
            ans[d-1] += 1
    for i in range(n-1):
        print(ans[i])
    return

=======
Suggestion 7

def main():
    N,X,Y = map(int,input().split())
    X-=1
    Y-=1
    dist = [0]*N
    for i in range(N):
        for j in range(i+1,N):
            dist[min(j-i,abs(X-i)+1+abs(Y-j))] += 1
    for i in range(1,N):
        print(dist[i])

=======
Suggestion 8

def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        n, path = queue.pop(0)
        if n == goal:
            return path
        else:
            for m in graph[n]:
                if m not in path:
                    queue.append((m, path+[m]))

=======
Suggestion 9

def solve():
    """
    頂点iと頂点jの距離がkになるような整数の組(i,j)(1≦i<j≦N)の数を求める
    """
    N, X, Y = map(int, input().split())
    ans = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j))
            ans[d] += 1
    for k in range(1, N):
        print(ans[k])

=======
Suggestion 10

def main():
    N,X,Y = map(int,input().split())

    for k in range(1,N):
        if k == 1:
            print(N-1)
        else:
            print((N-k)*(N-k-1)//2 - (N-Y-k+1)*(N-X-k+1) + (X-1)*(Y-k))
