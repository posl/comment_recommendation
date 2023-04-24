Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s == k:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    d = {}
    for i in range(N+1):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    ans = 0
    for i in range(N+1):
        if A[i] - K in d:
            ans += d[A[i] - K]
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    ans = 0
    d = {}
    for i in range(N+1):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    for i in range(N+1):
        if A[i] + K in d:
            ans += d[A[i] + K]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0]
    for i in range(N):
        S.append(S[-1] + A[i])
    # 累積和の値の出現回数
    ans = 0
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N+1):
        ans += d[S[i] - K]
        d[S[i]] += 1
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    d = {}
    d[0] = 1
    for i in range(n):
        s += a[i]
        if s - k in d:
            ans += d[s - k]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(ans)

main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    sum_list = [0]
    for i in range(N):
        sum_list.append(sum_list[i] + A[i])
    for i in range(N):
        for j in range(i + 1, N + 1):
            if sum_list[j] - sum_list[i] == K:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    #入力
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    
    #累積和
    s = [0]
    for i in range(N):
        s.append(s[i]+A[i])
    
    #辞書
    d = {}
    for i in range(N+1):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    
    #答え
    ans = 0
    for i in range(N+1):
        if s[i] - K in d:
            ans += d[s[i]-K]
    
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    # 連続部分列の和を求める。
    # 連続部分列の和がKになる場合は、
    # 連続部分列の和がKの倍数になる場合と、
    # 連続部分列の和がKの倍数になる場合との和となる。
    # 連続部分列の和がKの倍数になる場合は、
    # 連続部分列の和がKの倍数になる場合と、
    # 連続部分列の和がKの倍数になる場合との和となる。
    # 連続部分列の和がKの倍数になる場合は、
    # 連続部分列の和がKの倍数になる場合と、
    # 連続部分列の和がKの倍数になる場合との和となる。
    # 連続部分列の和がKの倍数になる場合は、
    # 連続部分列の和がKの倍数になる場合と、
    # 連続部分列の和がKの倍数になる場合との和となる。
    # 連続部分列の和がKの倍数になる場合は、
    # 連続部分列の和がKの倍数になる場合と、
    # 連続部分列の和がKの倍数になる場合との和となる。
    # 連続部分列の和がKの倍数になる場合は、
    # 連続部分列の和がKの倍数になる場合と、
    # 連続部分列の和がKの倍数になる場合との和となる。

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 連続部分列の和を求める
    # 例えば、A=[8,-3,5,7,0,-4] の場合
    # S=[8,5,10,17,17,13] となる
    # これは、A[0:2]の和、A[0:3]の和、A[0:4]の和、... となる
    S = [0]
    for i in range(N):
        S.append(S[-1]+A[i])
    # 連続部分列の和がKになる組み合わせを求める
    # 例えば、S=[8,5,10,17,17,13] で K=5 の場合
    # 8,5,10 と 5,10,17 の組み合わせがある
    # これは、S[0:3]とS[1:4]の和がKになることを意味する
    # これを、辞書型で管理する
    # 辞書のキーは連続部分列の和で、値はその和が出現する回数
    # 例えば、S=[8,5,10,17,17,13] で K=5 の場合
    # 8,5,10 の組み合わせは 1 組
    # 5,10,17 の組み合わせは 2 組
    # となるので、辞書は
    # {8:1, 5:1, 10:1, 17:2} となる
    # これを用いて、S[0:3]とS[1:4]の和がKになるか判定する
    # S[0:3] = 8+5+10 = 23
    # S[1:4] = 5+10+17

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #print(sum(A))
    #print(sum(A[1:2]))
    #print(sum(A[1:3]))
    #print(sum(A[1:4]))
    #print(sum(A[1:5]))
    #print(sum(A[1:6]))
    #print(sum(A[2:3]))
    #print(sum(A[2:4]))
    #print(sum(A[2:5]))
    #print(sum(A[2:6]))
    #print(sum(A[3:4]))
    #print(sum(A[3:5]))
    #print(sum(A[3:6]))
    #print(sum(A[4:5]))
    #print(sum(A[4:6]))
    #print(sum(A[5:6]))
    
    count = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum(A[i:j]) == K:
                count += 1
    print(count)
