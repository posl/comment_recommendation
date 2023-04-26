Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N):
        ans += (X[i] - X[N//2]) ** 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N):
        ans += X[i] * i - X[i] * (N - i - 1)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    X = list(map(int,input().split()))
    ans = 10**10
    for p in range(1,101):
        tmp = 0
        for x in X:
            tmp += (x-p)**2
        ans = min(ans,tmp)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 0
    for i in range(1, 101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i)**2
        if ans == 0:
            ans = tmp
        else:
            ans = min(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(n):
        ans += (i * x[i] - (n - i - 1) * x[i])
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    X = list(map(int,input().split()))
    X.sort()
    if N % 2 == 0:
        print(X[N//2] - X[N//2 - 1])
    else:
        print(0)

=======
Suggestion 7

def main():
    N = int(input())
    X = [int(x) for x in input().split()]
    X.sort()
    if N % 2 == 0:
        print(X[N//2] - X[N//2-1])
    else:
        print(0)

=======
Suggestion 8

def main():
    N = int(input())
    X = list(map(int, input().split()))

    X.sort()
    ans = 10**18
    for i in range(1, 101):
        tmp = 0
        for j in range(N):
            tmp += (X[j] - i)**2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    X = list(map(int, input().split()))

    #print(N)
    #print(X)

    #X.sort()
    #print(X)

    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                ans += (X[i] - X[j]) ** 2

    print(ans)

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    X = list(map(int, input().split()))

    #処理
    #全探索
    an
