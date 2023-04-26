Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(n):
        d_list.append(abs(x_list[i + 1] - x_list[i]))
    d = d_list[0]
    for i in range(1, n):
        d = gcd(d, d_list[i])
    print(d)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(X)
    x_list.sort()
    D_list = []
    for i in range(N):
        D_list.append(x_list[i+1] - x_list[i])
    D = D_list[0]
    for i in range(1, N):
        D = gcd(D, D_list[i])
    print(D)

=======
Suggestion 4

def main():
    N,X = map(int,input().split())
    x = list(map(int,input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1]-x[i])
    ans = d[0]
    for i in range(N-1):
        ans = gcd(ans,d[i+1])
    print(ans)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    xl = list(map(int, input().split()))

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    ans = abs(x - xl[0])
    for i in range(1, n):
        ans = gcd(ans, abs(x - xl[i]))

    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    y = []
    for i in range(N):
        y.append(x[i + 1] - x[i])
    ans = y[0]
    for i in range(N):
        ans = gcd(ans, y[i])
    print(ans)

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(n):
        d_list.append(x_list[i+1]-x_list[i])
    d = d_list[0]
    for i in range(1,n):
        d = gcd(d,d_list[i])
    print(d)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = [x_list[i+1] - x_list[i] for i in range(n)]
    if n == 1:
        print(d_list[0])
    else:
        d = d_list[0]
        for i in range(n-1):
            d = min(d, d_list[i+1])
        print(d)

=======
Suggestion 9

def gcd(a, b):
    if a%b == 0:
        return(b)
    else:
        return(gcd(b, a%b))
