Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    c = [0] * (n + 1)
    for i in range(n + 1):
        c[i] = b[i] - k
    d = [0] * (n + 1)
    for i in range(n + 1):
        d[i] = c[i] - i
    e = {}
    for i in range(n + 1):
        if d[i] in e:
            e[d[i]] += 1
        else:
            e[d[i]] = 1
    ans = 0
    for i in e:
        ans += e[i] * (e[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        s = 0
        for j in range(i, N):
            s += A[j]
            if s == K:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    ans = 0
    cnt = {}
    for i in range(N + 1):
        if A[i] - K in cnt:
            ans += cnt[A[i] - K]
        if A[i] in cnt:
            cnt[A[i]] += 1
        else:
            cnt[A[i]] = 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        sum = 0
        for j in range(i,N):
            sum += A[j]
            if sum == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d = {0: 1}
    s = 0
    ans = 0
    for i in range(N):
        s += A[i]
        ans += d.get(s - K, 0)
        d[s] = d.get(s, 0) + 1
    print(ans)

=======
Suggestion 6

def solve():
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
Suggestion 7

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    d = {0:1}
    for i in range(n):
        s += a[i]
        ans += d.get(s-k,0)
        d[s] = d.get(s,0)+1
    print(ans)
main()

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 累積和
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    
    # 累積和の差がKの倍数の個数
    from collections import Counter
    C = Counter(S)
    ans = 0
    for s in S:
        ans += C[s] * (C[s] - 1) // 2
        if (s - K) in C:
            ans -= C[s - K] * (C[s - K] - 1) // 2
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        r = l
        sum = 0
        while r < N:
            sum += A[r]
            if sum == K:
                ans += 1
            r += 1
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # iを固定してjを動かす
    # iとjの差がKになる組み合わせを数える
    # iとjの差がKになるというのは、jまでの累積和からiまでの累積和を引いた値がKになるということ
    # つまり、jまでの累積和がK+iになる組み合わせを数える
    # jまでの累積和がK+iになる組み合わせを数えるには、累積和の中でK+iがいくつあるかを数えればいい
    # つまり、累積和の中でK+iがいくつあるかを数える
    # これを辞書で管理する
    # 辞書のキーは累積和、値はその累積和が出現した回数
    # 例えば、累積和がK+iになる組み合わせを数えるときに、累積和がK+iになる組み合わせが2回あったとする
    # そのとき、辞書の値は2になる
    # 辞書の値を数え上げるのは、辞書の値の総和になる
    # ここで、累積和の中でK+iがいくつあるかを数えるときに、累積和がK+iになる組み合わせが2回あったとする
    # そのとき、累積和がK+iになる組み合わせは2通りある
    # それは、(K+i,K+i)と
