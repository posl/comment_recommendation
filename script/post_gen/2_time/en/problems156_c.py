Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = list(map(int, input().split()))

=======
Suggestion 2

def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 10**9
    for p in range(101):
        tmp = 0
        for x in X:
            tmp += (x - p)**2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    P = X[N // 2]
    ans = 0
    for i in range(N):
        ans += abs(X[i] - P)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10**10
    for i in range(min(x), max(x) + 1):
        ans = min(ans, sum([(j - i) ** 2 for j in x]))
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    x = sorted(x)
    ans = 0
    for i in range(n):
        ans += (x[i] - x[n // 2]) ** 2
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 1000000000000000000
    for i in range(1, 101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i) ** 2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    X = list(map(int, input().split()))

    ans = 0
    for i in range(1, N):
        ans += (X[i] - X[i-1])**2

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    X = list(map(int,input().split()))
    ans = 0
    for i in range(1,101):
        ans += sum([(X[j]-i)**2 for j in range(N)])
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    X = list(map(int,input().split()))
    ans = 0
    for i in range(1,101):
        ans += sum([(i-j)**2 for j in X])
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    #print(x)
    sum = 0
    for i in range(n-1):
        sum += x[i+1] - x[i]
    print(sum)

main()
