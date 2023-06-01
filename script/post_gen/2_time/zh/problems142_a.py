Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        a[-1] = a[-1]//2
        a.sort()
    print(sum(a))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    i = 0
    while m > 0:
        a[i] = a[i] // 2
        m -= 1
        i += 1
        if i == n:
            i = 0
    print(sum(a))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 4

def solve(n, m, a):
    a.sort()
    for i in range(m):
        a[-1] = a[-1] // 2
        a.sort()
    return sum(a)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        a[-1] = a[-1]//2
        a.sort()
    print(sum(a))

=======
Suggestion 6

def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    #print(a)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
        #print(a)
    print(sum(a))

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    for i in range(M):
        A[-1] = A[-1] // 2
        A.sort()
    print(sum(A))

=======
Suggestion 8

def buyGoods(N, M, A):
    #print(N, M, A)
    A.sort()
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
    if M >= sum:
        return 0
    else:
        for i in range(M):
            A[N-1-i] = A[N-1-i]//2
        return buyGoods(N, M, A)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # 二分探索
    def is_ok(arg):
        cnt = 0
        for i in range(n):
            cnt += max(0, a[i] - arg // 2)
        return cnt >= m

    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(0, 10 ** 9 + 1))

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    # 二分探索
    def is_ok(x):
        # 二分探索の判定部分
        cnt = 0
        for a in A:
            if a < x // 2:
                break
            cnt += min(a, x // 2)
        return cnt >= M * x

    def meguru_bisect(ng, ok):
        # 二分探索
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(0, 10 ** 18))
