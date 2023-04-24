Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N):
        ans += (X[i] - X[N // 2]) ** 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(n):
        ans += (x[i] - x[n // 2]) ** 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(1, 101):
        tmp = 0
        for j in range(N):
            tmp += (X[j] - i)**2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(1,N):
        ans += (X[i]-X[i-1])*(N-i)*i
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(n):
        ans += (i - n//2) * (x[i] - x[n//2])
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    #print(x)
    ans = 0
    for i in range(n):
        ans += (x[i] - x[n // 2]) ** 2
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += (X[i] - X[i // 2]) ** 2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    X = list(map(int, input().split()))

    X.sort()
    ans = 0
    for i in range(N):
        ans += X[i]*(N-1-i) - X[i]*i

    print(ans)
