Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum += i*100 + j
    print(sum)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    sum = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            sum += i*100+j
    print(sum)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    print(sum([i * 100 + j for i in range(1, N + 1) for j in range(1, K + 1)]))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    print(100*n*(n+1)//2*k)

=======
Suggestion 5

def problem203_b(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += i*100 + j
    return sum

=======
Suggestion 6

def solve():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            ans += i*100 + j
    print(ans)
solve()

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    print(100 * (n + 1) * n * k // 2)

=======
Suggestion 8

def prob_b():
    n,k = map(int,input().split())
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum = sum + i*100 + j
    print(sum)

=======
Suggestion 9

def getSum(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += i*100+j
    return sum

n,k = map(int, input().split())
print(getSum(n,k))

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            ans += i * 100 + j
    print(ans)
