Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[:K]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-k):
        ans += a[i]
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if K >= N:
        print(0)
        return
    print(sum(A[:N-K]))

=======
Suggestion 4

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 1:
        print(n)
        return
    if k == n:
        print(1)
        return
    if n == 2:
        if a[0] == a[1]:
            print(1)
        else:
            print(2)
        return
    if k == 2:
        a = list(set(a))
        cnt = 0
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                cnt += 1
        print(n-cnt)
        return
    if k == 3:
        a = list(set(a))
        cnt = 0
        for i in range(len(a)-2):
            if a[i] == a[i+1]-1 and a[i+1] == a[i+2]-1:
                cnt += 1
        print(n-cnt)
        return

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-K])

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    #print(a)
    ans = 0
    for i in range(n):
        if i < k:
            continue
        ans += a[i]
    print(ans)

=======
Suggestion 7

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    print(sum(A[:K]))
    return 0

=======
Suggestion 8

def solve():
    pass
