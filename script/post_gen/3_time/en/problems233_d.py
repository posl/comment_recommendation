Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    cnt = 0
    for i in range(N+1):
        for j in range(i+1, N+1):
            if A[j]-A[i] == K:
                cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]

    ans = 0
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N+1):
        d[A[i]] += 1
        if A[i] - K in d:
            ans += d[A[i] - K]
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum == K:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(n):
        a[i+1] += a[i]
    aa = sorted(a)
    ans = 0
    for i in range(n):
        l = i
        r = n - 1
        while r - l > 1:
            mid = (l + r) // 2
            if aa[mid] - aa[i] < k:
                l = mid
            else:
                r = mid
        if aa[r] - aa[i] == k:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1]+a[i])
    d = {}
    for i in range(n+1):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    ans = 0
    for i in range(n+1):
        if s[i]+k in d:
            ans += d[s[i]+k]
    print(ans)

=======
Suggestion 6

def main():
    import sys
    readline = sys.stdin.readline
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    cnt = 0
    for i in range(N):
        for j in range(i, N):
            if sum(A[i:j+1]) == K:
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    A = [a%K for a in A]
    cnt = 0
    dic = {}
    for a in A:
        if a in dic:
            cnt += dic[a]
            dic[a] += 1
        else:
            dic[a] = 1
    print(cnt)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        a[i] = a[i] - k
    s = 0
    ans = 0
    for i in range(n):
        s += a[i]
        if s == 0:
            ans += 1
        if s in d:
            ans += d[s]
            d[s] += 1
        else:
            d[s] = 1
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # A[i]からA[j]までの和がKとなるような(i,j)の組み合わせを求める
    # A[i]からA[j]までの和は、A[0]からA[j]までの和からA[0]からA[i-1]までの和を引くことで求められる
    # つまり、A[i]からA[j]までの和がKとなるような(i,j)の組み合わせは、A[0]からA[j]までの和がKとなるような(j)の個数からA[0]からA[i-1]までの和がKとなるような(i-1)の個数を引くことで求められる
    # このような(i,j)の組み合わせを求めるために、累積和を求める
    # 累積和は、A[0]からA[i]までの和をA[i]に格納することで求めることができる
    # ここで、A[0]からA[i]までの和がKとなるような(i)の個数を求める
    # このような(i)の個数を求めるために、A[i]をキーとして、A[i]が何回出現するかを記録する辞書を用意する
    # このとき、A[i]が出現する回数を求めるために、A[i]をキーとして、A[i]が何回出現するかを記録する辞書を用意する
    # ここで、A[i]が出現する回数を求めるために、A[i]をキーとして、A[i]が何回出現するかを記

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # A[i]からA[j]までの和をsum[i][j]とする
    sum = [[0 for i in range(N)] for j in range(N)]
    ans = 0
    for i in range(N):
        sum[i][i] = A[i]
        if sum[i][i] == K:
            ans += 1
        for j in range(i+1, N):
            sum[i][j] = sum[i][j-1] + A[j]
            if sum[i][j] == K:
                ans += 1
    print(ans)
