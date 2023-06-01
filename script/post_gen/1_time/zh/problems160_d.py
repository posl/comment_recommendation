Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,x,y = map(int, input().split())
    x -= 1
    y -= 1
    ans = [0]*(n-1)
    for i in range(n):
        for j in range(i+1, n):
            d = min(j-i, abs(x-i)+abs(y-j)+1)
            ans[d-1] += 1
    for i in range(n-1):
        print(ans[i])

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    ans = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            ans[min(j - i, abs(x - i) + 1 + abs(j - y), abs(y - i) + 1 + abs(j - x))] += 1
    for i in range(1, n):
        print(ans[i])

=======
Suggestion 4

def main():
    n,x,y = map(int,input().split())
    #print(n,x,y)
    #print(type(n),type(x),type(y))
    #print(type(n))
    #print(type(x))
    #print(type(y))
    #print(n,x,y)
    #print(type(n),type(x),type(y))
    #print(type(n))
    #print(type(x))
    #print(type(y))
    #print(n,x,y)
    #print(type(n),type(x),type(y))
    #print(type(n))
    #print(type(x))
    #print(type(y))
    #print(n,x,y)
    #print(type(n),type(x),type(y))
    #print(type(n))
    #print(type(x))
    #print(type(y))
    #print(n,x,y)
    #print(type(n),type(x),type(y))
    #print(type(n))
    #print(type(x))
    #print(type(y))
    #print(n,x,y)
    #print(type(n),type(x),type(y))
    #print(type(n))
    #print(type(x))
    #print(type(y))
    #print(n,x,y)
    #print(type(n),type(x),type(y))
    #print(type(n))
    #print(type(x))
    #print(type(y))
    #print(n,x,y)
    #print(type(n),type(x),type(y))
    #print(type(n))
    #print(type(x))
    #print(type(y))

=======
Suggestion 5

def main():
    n, x, y = map(int, input().split())
    for k in range(1, n):
        ans = 0
        for i in range(1, n):
            for j in range(i+1, n+1):
                if i <= x and j >= y:
                    d = min(j-i, abs(i-x)+1+abs(j-y))
                elif i <= x:
                    d = min(j-i, abs(i-x)+1+abs(j-y))
                elif j >= y:
                    d = min(j-i, abs(i-x)+1+abs(j-y))
                else:
                    d = j-i
                if d == k:
                    ans += 1
        print(ans)

=======
Suggestion 6

def main():
    N,X,Y = map(int,input().split())
    ans = [0 for i in range(N)]
    for i in range(1,N):
        for j in range(i+1,N+1):
            ans[min(j-i,abs(X-i)+abs(Y-j)+1)] += 1
    for i in range(1,N):
        print(ans[i])

=======
Suggestion 7

def main():
    n,x,y = map(int, input().split())
    ans = [0] * n
    for i in range(1,n):
        for j in range(i+1,n+1):
            ans[min(j-i,abs(x-i)+1+abs(y-j))] += 1
    for i in range(1,n):
        print(ans[i])

=======
Suggestion 8

def main():
    n,x,y = map(int, input().split())
    n -= 1
    x -= 1
    y -= 1
    ans = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            ans[min(j-i,abs(x-i)+1+abs(y-j))] += 1
    for i in range(1,n):
        print(ans[i])

=======
Suggestion 9

def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    ans = [0] * (n - 1)
    for i in range(n):
        for j in range(i + 1, n):
            d = min(j - i, abs(x - i) + 1 + abs(y - j))
            ans[d - 1] += 1
    for i in range(n - 1):
        print(ans[i])
