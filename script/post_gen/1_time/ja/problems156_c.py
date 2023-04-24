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
    N = int(input())
    X = list(map(int, input().split()))
    ans = 10**10
    for p in range(1, 101):
        tmp = 0
        for x in X:
            tmp += (x - p)**2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(1, 101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i)**2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(1, n):
        ans += (x[i] - x[i - 1]) * i * (n - i)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N):
        ans += X[i] * (i - N // 2) * 2
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    print(sum([abs(x[i]-x[n//2]) for i in range(n)]))

=======
Suggestion 7

def main():
    #入力
    n = int(input())
    x = list(map(int, input().split()))
    #処理
    ans = 10**9
    for i in range(1, 101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i)**2
        ans = min(ans, tmp)
    #出力
    print(ans)
