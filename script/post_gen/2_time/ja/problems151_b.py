Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n * m - sum(a) <= k:
        print(max(n * m - sum(a), 0))
    else:
        print(-1)

=======
Suggestion 2

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        sum += a[i]
    if n*m - sum <= k:
        print(max(0, n*m - sum))
    else:
        print(-1)

=======
Suggestion 3

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    x = n * m - sum(a)
    if x > k:
        print(-1)
    elif x < 0:
        print(0)
    else:
        print(x)

=======
Suggestion 4

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n*m - sum(a) > k:
        print(-1)
    else:
        print(max(n*m - sum(a), 0))

=======
Suggestion 5

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n*m-sum(a) > k:
        print(-1)
    elif n*m-sum(a) < 0:
        print(0)
    else:
        print(n*m-sum(a))

=======
Suggestion 6

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n*m-sum(a) <= k:
        print(max(0,n*m-sum(a)))
    else:
        print(-1)

=======
Suggestion 7

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    target = N * M
    if total >= target:
        print(0)
    elif total + K < target:
        print(-1)
    else:
        print(target - total)

=======
Suggestion 8

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    if N*M - sum_A <= K:
        if N*M - sum_A > 0:
            print(N*M - sum_A)
        else:
            print(0)
    else:
        print(-1)

=======
Suggestion 9

def main():
    n,k,m = map(int, input().split())
    a = list(map(int, input().split()))
    if (n*m - sum(a)) <= k:
        print(max(0,n*m - sum(a)))
    else:
        print(-1)

=======
Suggestion 10

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    sumA = sum(A)
    #print(sumA)
    need = N * M - sumA
    #print(need)

    if need <= K:
        print(max(0, need))
    else:
        print(-1)
