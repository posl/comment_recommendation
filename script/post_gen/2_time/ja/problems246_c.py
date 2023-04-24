Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] < X:
                ans += A[i]
            else:
                ans += X
                K -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            ans += max(A[i] - X, 0)
            K -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 3

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] < X:
                ans += A[i]
            else:
                if K > 1:
                    ans += X
                    K -= 2
                else:
                    ans += A[i]
                    K -= 1
        else:
            ans += A[i]
    print(ans)

main()

=======
Suggestion 4

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            ans += max(A[i] - X, 0)
            K -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 5

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(a[i] - x, 0)
            k -= 1
        else:
            ans += a[i]
    print(ans)

main()

=======
Suggestion 6

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    total = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                total += X
                K -= 1
            else:
                total += A[i]
        else:
            total += A[i]
    print(total)

=======
Suggestion 7

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                ans += A[i] - X
                K -= 1
            else:
                ans += A[i]
        else:
            ans += A[i]

    print(ans)

=======
Suggestion 8

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        if A[i] < X:
            cnt += 1
        else:
            break
    if K >= cnt:
        print(0)
    else:
        print(sum(A[:N - K]))

=======
Suggestion 9

def get_input():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, x, a

=======
Suggestion 10

def main():
    n,k,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    for i in range(n):
        if k>0:
            if a[i]>x:
                ans+=x
                k-=1
            else:
                ans+=a[i]
        else:
            ans+=a[i]
    print(ans)
