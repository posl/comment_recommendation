Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if k <= n:
        for i in range(n):
            if i < k:
                print(1)
            else:
                print(0)
        return

    k -= n
    m = k // (n - 1)
    k -= m * (n - 1)

    for i in range(n):
        if i == 0:
            print(m + 1)
        else:
            if i <= k:
                print(m + 2)
            else:
                print(m + 1)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if K <= N:
        for i in range(N):
            if i < K:
                print(K // N + 1)
            else:
                print(K // N)
    else:
        for i in range(N):
            if i < N - 1:
                print(a[i] + (K - N) // N)
            else:
                print(a[i] + (K - N) // N + (K - N) % N)

main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * N
    for i in range(N):
        b[i] = a[i] - 1
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
    for i in range(K % N):
        ans[i] += 1
    for i in range(N):
        print(ans[b[i]])

=======
Suggestion 5

def main():
    #N:国民の人数
    #K:高橋君が持っているお菓子の個数
    N, K = map(int, input().split())
    #a:国民の国民番号
    a = list(map(int, input().split()))
    #aを国民番号の昇順にソート
    a.sort()
    #KをNで割った商と余りを求める
    quo = K // N
    rem = K % N
    #余りが0なら全員にquo個ずつ配る
    if rem == 0:
        for i in range(N):
            print(quo)
    #余りが0でないなら
    else:
        #余りの数だけa[0]からa[rem-1]までの国民に1個ずつ配る
        for i in range(rem):
            print(quo+1)
        #余りの数だけa[rem]からa[N-1]までの国民にquo個ずつ配る
        for i in range(rem, N):
            print(quo)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    ans[0] = K // N
    K %= N
    for i in range(K):
        ans[a.index(i+1)] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    a = sorted(A)
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
        if K % N > i:
            ans[i] += 1
    for i in range(N):
        ans[A.index(a[i])] += ans[i]
        ans[i] = 0
    for i in range(N):
        print(ans[i])

=======
Suggestion 8

def main():
    import sys
    from io import StringIO
    import unittest

    def resolve():
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        A.sort()
        for i in range(N):
            if K <= A[i]:
                print(K)
                K = 0
            else:
                print(A[i])
                K -= A[i]
        for i in range(N):
            print(K // (N - i), end=' ')
            K -= K // (N - i)

    # -----------------------------

    if sys.argv[-1] == 'ONLINE_JUDGE':
        resolve()
    else:
        sys.stdin = StringIO("""\
2 7
1 8
        """)
        unittest.main()

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    k = K
    if k <= N:
        for i in range(N):
            if i < k:
                print(1)
            else:
                print(0)
    else:
        k -= N
        for i in range(N):
            if i == 0:
                print(k // N + 1)
            else:
                print(k // N)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    #print(A)
    B = []
    for i in range(1, N+1):
        B.append(A[i] - A[i-1] - 1)
    #print(B)
    ans = []
    for i in range(N):
        ans.append((K - 1) // N + 1)
    #print(ans)
    for i in range(N):
        if (K - 1) // N + 1 > B[i]:
            K -= B[i]
            ans[i] += B[i]
        else:
            ans[i] += (K - 1) % N
            break
    for i in range(N):
        print(ans[i])
