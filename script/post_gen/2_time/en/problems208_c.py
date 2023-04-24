Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if K <= N:
        for i in range(N):
            print(K)
    else:
        K -= N
        a.append(10 ** 9 + 1)
        ans = [0] * N
        for i in range(N):
            if a[i + 1] - a[i] == 1:
                ans[i] = K // N
            else:
                ans[i] = K // (N - i)
                break
        for i in range(N):
            print(ans[i] + N // N)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * (N + 1)
    for i in range(N):
        b[i + 1] = b[i] + a[i]
    for i in range(N):
        if K >= (N - i) * a[i] - (b[N] - b[i]):
            print(K // (N - i))
            exit()
        K -= a[i]

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if K <= N:
        for i in range(N):
            print(K)
        return

    K -= N
    cnt = [0] * N
    for i in range(1, N):
        cnt[i] = cnt[i-1] + (a[i] - a[i-1]) * i
    cnt.append(K + 1)

    start = 0
    end = N
    while end - start > 1:
        mid = (start + end) // 2
        if cnt[mid] <= K:
            start = mid
        else:
            end = mid

    ans = [0] * N
    for i in range(N):
        ans[i] = (K - cnt[start]) // (start + 1) + a[i]
    for i in range(K - cnt[start] - (K - cnt[start]) // (start + 1) * (start + 1)):
        ans[i] += 1

    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = [0] * N
    for i in range(N):
        C[i] = B.index(A[i])
    D = [0] * N
    for i in range(N):
        D[C[i]] = i
    E = [0] * N
    for i in range(N):
        E[i] = (K - 1) // N
    F = (K - 1) % N
    for i in range(F):
        E[D[i]] += 1
    for i in range(N):
        print(E[i] + 1)

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    for i in range(1, N+1):
        A[i] -= i
    A.append(10**10)
    L = 0
    R = 10**9
    while R-L > 1:
        M = (L+R)//2
        if A[M] <= K:
            L = M
        else:
            R = M
    for i in range(1, N+1):
        if A[i] <= K:
            print(K//L)
        else:
            print(K//L + 1)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    if k >= n:
        for i in range(n):
            ans[i] += k // n
        k = k % n
    for i in range(k):
        ans[i] += 1
    for i in range(n):
        print(ans[i] + (k + a[i] - 1) // a[i])

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] = K//N
        if K%N > i:
            ans[i] += 1
    for i in range(N):
        if A[i] <= K%N:
            ans[i] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    for i in range(N):
        if K <= (A[i + 1] - A[i] - 1) * (i + 1):
            break
        else:
            K -= (A[i + 1] - A[i] - 1) * (i + 1)
    print(K // (i + 1) + A[i])
    for j in range(i + 1, N):
        print(K // (i + 1) + A[i] + K % (i + 1) - (j - i) * (A[j] - A[j - 1] - 1))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    # 1人あたりの平均値を求める
    ave = K // N
    # 余りを求める
    mod = K % N
    # aの中でmod以上の値の数を求める
    cnt = 0
    for i in range(N):
        if a[i] <= mod:
            cnt += 1

    # 出力
    for i in range(N):
        if a[i] <= mod:
            print(ave + 1)
        else:
            print(ave)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(N, K)
    #print(A)

    # A[i] = i+1番目の人が持っているスイーツの数
    # A[i] = A[i-1] + 1
    # A[i] = A[i-1] + N
    # A[i] = A[i-1] + N - (i-1)
    # A[i] = A[i-1] + N - i + 1
    # A[i] = A[i-1] + N - i + 1
    # A[i] = A[i-1] + N - i + 1

    # N人に1個ずつ配る
    # N人に2個ずつ配る
    # N人に3個ずつ配る
    # N人に4個ずつ配る
    # N人に5個ずつ配る
    # N人に6個ずつ配る
    # N人に7個ずつ配る
    # N人に8個ずつ配る
    # N人に9個ずつ配る
    # N人に10個ずつ配る
    # N人に11個ずつ配る
    # N人に12個ずつ配る
    # N人に13個ずつ配る
    # N人に14個ずつ配る
    # N人に15個ずつ配る
    # N人に16個ずつ配る
    # N人に17個ずつ配る
    # N人に18個ずつ配る
    # N人に19個ずつ配る
    # N人に20個ずつ配る
    # N人に21個ずつ配る
    # N人に22個ずつ配る
    # N人に23個ずつ配る
    # N人に24
