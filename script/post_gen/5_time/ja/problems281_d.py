Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    count = 0
    for i in range(K):
        count += A[i]

    if count == 0:
        print(0)
        return

    if count % D != 0:
        print(count)
        return

    if count // D == 1:
        print(-1)
        return

    print(count - 1)

=======
Suggestion 2

def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    max_sum = 0
    for i in range(n-k+1):
        s = sum(a[i:i+k])
        if s % d == 0:
            max_sum = max(max_sum, s)
    if max_sum == 0:
        print(-1)
    else:
        print(max_sum)

=======
Suggestion 3

def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))

    # n, k, d = 4, 2, 2
    # a = [1, 2, 3, 4]

    # n, k, d = 3, 1, 2
    # a = [1, 3, 5]

    # n, k, d = 100, 100, 100
    # a = [0] * n
    # for i in range(n):
    #     a[i] = i + 1

    # n, k, d = 100, 100, 2
    # a = [0] * n
    # for i in range(n):
    #     a[i] = i + 1

    # n, k, d = 100, 100, 3
    # a = [0] * n
    # for i in range(n):
    #     a[i] = i + 1

    # n, k, d = 100, 100, 4
    # a = [0] * n
    # for i in range(n):
    #     a[i] = i + 1

    # n, k, d = 100, 100, 5
    # a = [0] * n
    # for i in range(n):
    #     a[i] = i + 1

    # n, k, d = 100, 100, 6
    # a = [0] * n
    # for i in range(n):
    #     a[i] = i + 1

    # n, k, d = 100, 100, 7
    # a = [0] * n
    # for i in range(n):
    #     a[i] = i + 1

    # n, k, d = 100, 100, 8
    # a = [0] * n
    # for i in range(n):
    #     a[i] = i + 1

    # n, k, d = 100, 100, 9
    # a = [0] * n
    # for i in range(n

=======
Suggestion 4

def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = -1
    if n >= k:
        for i in range(n-k+1):
            if a[i] % d == 0:
                ans = a[i]
                break
    print(ans)

=======
Suggestion 5

def main():
    n,k,d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 1:
        if a[0] % d == 0:
            print(a[0])
        else:
            print(-1)
        return

    if n < k:
        print(-1)
        return

    if a[0] % d == 0:
        print(a[0] + d * (k-1))
        return

    for i in range(n-k+1):
        if a[i] % d == 0:
            print(a[i] + d * (k-1))
            return

    print(-1)
    return

=======
Suggestion 6

def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    max_sum = 0
    for i in range(k):
        max_sum += a[i]
    if max_sum % d == 0:
        print(max_sum)
    else:
        for i in range(k, n):
            if a[i] < d:
                max_sum += a[i]
                if max_sum % d == 0:
                    print(max_sum)
                    exit()
        print(-1)

=======
Suggestion 7

def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    s = 0
    for i in range(n-k+1):
        if a[i] % d == 0:
            s = max(s,a[i])
    if s == 0:
        print(-1)
    else:
        print(s)

=======
Suggestion 8

def solve():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if N < K:
        print("-1")
        return
    if K == 1:
        if A[0] % D == 0:
            print("-1")
        else:
            print(A[0])
        return
    ans = -1
    for i in range(N-K+1):
        if A[i] % D == 0:
            continue
        ans = max(ans, A[i+K-1])
    print(ans)
    return

=======
Suggestion 9

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    S = set()
    for i in range(K):
        S.add(A[i])
    if len(S) == 1:
        print(-1)
    else:
        print(max(S))

=======
Suggestion 10

def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    ans = -1
    for i in range(n-k+1):
        if (a[i]-a[i+k-1])%d == 0:
            ans = max(ans,a[i+k-1])
    print(ans)
