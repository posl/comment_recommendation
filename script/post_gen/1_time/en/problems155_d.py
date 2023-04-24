Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(A[K-1])
        return
    if A[-1] <= 0:
        if K%2 == 0:
            print(-A[N-K])
        else:
            print(A[N-K])
        return
    A = [abs(a) for a in A]
    A.sort()
    A = [a*(-1) if i%2 == 0 else a for i, a in enumerate(A)]
    A.sort()
    print(A[K-1])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(A[K - 1])
        return
    if A[-1] <= 0:
        print(A[N - K])
        return
    if K == N * (N - 1) // 2:
        print(A[-1] * A[-2])
        return
    def is_ok(x):
        cnt = 0
        j = N - 1
        for i in range(N):
            while j > i and A[i] * A[j] > x:
                j -= 1
            cnt += j - i
        return cnt >= K
    ng = -1
    ok = 10 ** 18
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    if A[0] >= 0:
        print(A[K-1])
        return
    if A[-1] <= 0:
        if K % 2 == 0:
            print(A[-K])
        else:
            print(A[K-1])
        return
    if K % 2 == 0:
        K = K // 2
        ans = 1
        for i in range(N):
            if A[i] <= 0:
                ans *= A[i]
                K -= 1
                if K == 0:
                    print(ans)
                    return
            else:
                break
        ans = 1
        for i in range(N-1, -1, -1):
            if A[i] >= 0:
                ans *= A[i]
                K -= 1
                if K == 0:
                    print(ans)
                    return
            else:
                break
        print(A[K-1])
        return
    else:
        ans = 1
        for i in range(N):
            if A[i] <= 0:
                ans *= A[i]
                K -= 1
                if K == 0:
                    print(ans)
                    return
            else:
                break
        ans = 1
        for i in range(N-1, -1, -1):
            if A[i] >= 0:
                ans *= A[i]
                K -= 1
                if K == 0:
                    print(ans)
                    return
            else:
                break
        print(A[K-1])
        return

=======
Suggestion 4

def get_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a for a in A if a < 0]
    B = [a for a in A if a < 0]
    C = [a for a in A if a >= 0]
    if not B:
        if K % 2 == 0:
            print(C[(K // 2) - 1] * C[K // 2])
        else:
            print(C[K // 2] * C[K // 2])
    elif not C:
        if K % 2 == 0:
            print(B[-(K // 2)] * B[-(K // 2) - 1])
        else:
            print(B[-(K // 2) - 1] * B[-(K // 2) - 1])
    else:
        ans = []
        for i in range(len(B)):
            for j in range(len(C)):
                ans.append(B[i] * C[j])
        ans.sort()
        print(ans[K - 1])

=======
Suggestion 6

def func(N, K, A):
    A.sort()
    if A[0] >= 0:
        return A[K-1]
    elif A[N-1] <= 0:
        if (K % 2) == 0:
            return A[N-1]
        else:
            return A[N-2]
    else:
        left = 0
        right = N-1
        while True:
            mid = (left + right) // 2
            if A[mid] >= 0:
                right = mid
            else:
                left = mid
            if right - left == 1:
                break
        # print(left, right)
        if (K % 2) == 0:
            if A[left] * A[left+1] >= A[right-1] * A[right]:
                return A[left] * A[left+1]
            else:
                return A[right-1] * A[right]
        else:
            if A[left] * A[left+1] >= A[right-1] * A[right]:
                return A[right-1] * A[right]
            else:
                return A[left] * A[left+1]

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    A = [A[i] * A[i + 1] for i in range(N)]
    A.sort()
    print(A[K - 1])

=======
Suggestion 8

def check(n, k, a):
    b = sorted(a)
    c = []
    for i in range(n):
        for j in range(i + 1, n):
            c.append(b[i] * b[j])
    c = sorted(c)
    return c[k - 1]

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(check(n, k, a))

=======
Suggestion 9

def get_num():
    return int(input())
