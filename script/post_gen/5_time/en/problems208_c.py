Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [k // n] * n
    k %= n
    for i in range(k):
        b[i] += 1
    for i in range(n):
        print(b[a.index(a[i])])

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [k//n] * n
    k %= n
    for i in range(k):
        ans[i] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    result = [k // n] * n
    k %= n
    for i in range(k):
        result[i] += 1
    for i in range(n):
        print(result[i])

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = [k // n] * n
    k = k % n
    for i in range(k):
        res[i] += 1
    for i in range(n):
        print(res[i])

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    q = k//n
    r = k%n
    for i in range(n):
        if i < r:
            print(q+1)
        else:
            print(q)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    for i in range(N):
        if K >= N:
            print(1)
        else:
            print(0)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    k1 = k//n
    k2 = k%n
    for i in range(n):
        if i < k2:
            print(k1+1)
        else:
            print(k1)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0]*N
    for i in range(N):
        if K >= N:
            ans[i] = 1
        else:
            ans[i] = 0
        K = max(0, K-1)
    for i in range(N):
        print(ans[i])

main()

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    # まずは全員に均等に配る
    for i in range(N):
        a[i] += K // N

    # 残りの配る数
    K = K % N

    # 配る
    for i in range(K):
        # 最小の人に配る
        m = min(a)
        for j in range(N):
            if a[j] == m:
                a[j] += 1
                break

    for i in range(N):
        print(a[i])
