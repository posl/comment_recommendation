Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        s = 0
        for j in range(i,n):
            s += a[j]
            if s == k:
                ans += 1
    print(ans)
main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        total = 0
        for j in range(i, N):
            total += A[j]
            if total == K:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    s = 0
    d = {0: 1}
    for a in A:
        s += a
        ans += d.get(s - K, 0)
        d[s] = d.get(s, 0) + 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    #累積和を求める
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    #累積和の差分を求める
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = S[i + 1] - K

    #累積和の差分をソート
    D.sort()

    #累積和の差分の同じものを探す
    ans = 0
    i = 0
    while i < N:
        cnt = 1
        while i < N and D[i] == D[i + 1]:
            cnt += 1
            i += 1
        ans += cnt * (cnt - 1) // 2
        i += 1

    print(ans)

=======
Suggestion 5

def main():
    # 入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    s = [0]
    for i in range(N):
        s.append(s[i] + A[i])
    # 累積和の差分について、差分がKになる組み合わせをカウント
    from collections import Counter
    c = Counter(s)
    ans = 0
    for k, v in c.items():
        ans += v * (v - 1) // 2
        if k + K in c:
            ans += v * c[k + K]
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    #累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    #print(S)
    #累積和の差分
    S_diff = [0] * (N + 1)
    for i in range(N):
        S_diff[i + 1] = S[i + 1] - K
    #print(S_diff)
    #累積和の差分の要素の出現回数
    S_diff_count = {}
    for i in range(N + 1):
        S_diff_count[S_diff[i]] = S_diff_count.get(S_diff[i], 0) + 1
    #print(S_diff_count)
    for v in S_diff_count.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    #累積和を作成
    S = [0] * (N+1)
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i-1]

    #累積和の差分がKとなる組の数をカウント
    from collections import defaultdict
    D = defaultdict(int)
    ans = 0
    for i in range(N+1):
        ans += D[S[i] - K]
        D[S[i]] += 1
    
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #Aの累積和を求める
    s = [0]*(N+1)
    for i in range(N):
        s[i+1] = s[i] + A[i]
    #累積和の値をキーに、その値が出現するインデックスを値とする辞書を作成
    d = {}
    for i in range(N+1):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    #累積和の値にKを足した値が辞書のキーに存在するかを確認
    #存在する場合、そのキーに対応するインデックスの組み合わせをカウントする
    ans = 0
    for i in range(N+1):
        if s[i]+K in d:
            ans += len(d[s[i]+K])
    print(ans)

=======
Suggestion 9

def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N,K,A)
    #print(type(N),type(K),type(A))
    #print(type(A[0]))
    #print("A[0]=",A[0])
    
    #連続部分列の和がKになる組み合わせの個数を求める
    #l,rを固定して、sum(A[l:r+1])を計算する
    #l,rを1つずつ増やしていくと、O(N^2)で計算できるが、TLEになる
    #sum(A[l:r+1]) = sum(A[0:r+1]) - sum(A[0:l])
    #sum(A[0:r+1])を計算しておき、sum(A[0:l])を引くことで、O(N)で計算できる
    #sum(A[0:l])は、sum(A[0:l-1])にA[l-1]を足したものと一致する
    #sum(A[0:l])を計算しておくために、Aの累積和を計算する
    #A[0]は0としておく
    #A[0] = 0
    #A_cum = [0]*(N+1)
    #for i in range(N):
    #    A_cum[i+1] = A_cum[i] + A[i]
    #print(A_cum)
    
    #sum(A[0:l])を計算しておくために、Aの累積和を計算する
    #A[0]は0としておく
    A_cum = [0]
    for i in range(N):
        A_cum.append(A_cum[i] + A[i])
    #print(A_cum)
    
    #sum(A[l:r+1]) = sum(A[0:r+1]) - sum(A[0:l])
    #sum(A[0:r+1]) = K + sum(A[0:l])
    #sum(A[0:l]) = sum(A[0:r+1]) - K
    #sum(A[0:l

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #前処理
    #累積和をとる
    S = [0]
    for i in range(N):
        S.append(S[-1]+A[i])
    #print(S)
    #累積和の差をとる
    T = []
    for i in range(N):
        T.append(S[i+1]-K)
    #print(T)
    #Tの要素をソートする
    T.sort()
    #print(T)
    #Tの要素の個数をカウントする
    #同じ要素の個数をカウントする
    #print(T.count(T[0]))
    ans = 0
    for i in range(N):
        ans += T.count(T[i])
    print(ans)
