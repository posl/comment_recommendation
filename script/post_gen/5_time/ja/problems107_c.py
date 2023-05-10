Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, abs(X[i])+abs(X[i]-X[i+K-1]))
        ans = min(ans, abs(X[i+K-1])+abs(X[i]-X[i+K-1]))
    print(ans)
main()

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if x[i] <= 0 and x[i+K-1] <= 0:
            tmp = abs(x[i])
        elif x[i] <= 0 and x[i+K-1] > 0:
            tmp = abs(x[i])*2 + x[i+K-1]
        else:
            tmp = x[i+K-1]
        ans = min(ans,tmp)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if X[i] <= 0 and X[i+K-1] <= 0:
            ans = min(ans, abs(X[i]))
        elif X[i] <= 0 and X[i+K-1] >= 0:
            ans = min(ans, abs(X[i])*2 + X[i+K-1])
        elif X[i] >= 0 and X[i+K-1] >= 0:
            ans = min(ans, X[i+K-1])
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, abs(x[i])+abs(x[i]-x[i+k-1]))
        ans = min(ans, abs(x[i+k-1])+abs(x[i]-x[i+k-1]))
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**10
    for i in range(n-k+1):
        if x[i]*x[i+k-1] > 0:
            ans = min(ans,max(abs(x[i]),abs(x[i+k-1])))
        else:
            ans = min(ans,x[i+k-1]-x[i]+min(abs(x[i]),abs(x[i+k-1])))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if X[i] < 0 and X[i+K-1] < 0:
            ans = min(ans, -X[i])
        elif X[i] < 0 and X[i+K-1] >= 0:
            ans = min(ans, -X[i]*2+X[i+K-1])
        elif X[i] >= 0 and X[i+K-1] >= 0:
            ans = min(ans, X[i+K-1])
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    #print(n, k)
    #print(x)
    ans = 10**9
    for i in range(n-k+1):
        #print(i)
        if x[i] <= 0 and x[i+k-1] <= 0:
            ans = min(ans, abs(x[i]))
        elif x[i] <= 0 and x[i+k-1] >= 0:
            ans = min(ans, abs(x[i])*2 + abs(x[i+k-1]))
        elif x[i] >= 0 and x[i+k-1] >= 0:
            ans = min(ans, abs(x[i+k-1]))
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if X[i] < 0 and X[i+K-1] < 0:
            ans = min(ans, -X[i])
        elif X[i] < 0 and X[i+K-1] >= 0:
            ans = min(ans, -X[i]*2+X[i+K-1])
        else:
            ans = min(ans, X[i+K-1])
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    ans = 10**9
    for i in range(N-K+1):
        left = X[i]
        right = X[i+K-1]
        if left < 0 and right < 0:
            ans = min(ans, abs(left))
        elif left < 0 and right >= 0:
            ans = min(ans, abs(left)*2 + abs(right))
        else:
            ans = min(ans, abs(right))
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        left = x[i]
        right = x[i + K - 1]
        ans = min(ans, right - left + min(abs(left), abs(right)))
    print(ans)
