Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    D = dict()
    for i in range(N+1):
        if S[i] in D:
            D[S[i]] += 1
        else:
            D[S[i]] = 1
    ans = 0
    for i in range(N+1):
        if S[i] + K in D:
            ans += D[S[i]+K]
    print(ans)

=======
Suggestion 2

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
Suggestion 3

def main():
    # 入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 累積和を求める
    S = [0]
    for i in range(N):
        S.append(S[-1] + A[i])
    
    # 累積和の差が K になる組の数をカウント
    # そのためには、各要素が何個あるかをカウントする
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N+1):
        d[S[i]] += 1
    
    # 組の数をカウント
    ans = 0
    for i in range(N+1):
        ans += d[S[i]] * (d[S[i]] - 1) // 2
    
    # 出力
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0

    #累積和
    S = [0]
    for i in range(N):
        S.append(S[i]+A[i])

    #累積和の差がKになる組み合わせを探す
    for i in range(N):
        for j in range(i+1, N+1):
            if S[j]-S[i] == K:
                ans += 1

    print(ans)

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0]*N
    S[0] = A[0]
    for i in range(1, N):
        S[i] = S[i-1] + A[i]
    d = dict()
    d[0] = 1
    ans = 0
    for i in range(N):
        if S[i] - K in d:
            ans += d[S[i] - K]
        if S[i] in d:
            d[S[i]] += 1
        else:
            d[S[i]] = 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    #累積和のリストを作る
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])

    #辞書を作る
    D = {}
    for i in range(N+1):
        if S[i] in D:
            D[S[i]].append(i)
        else:
            D[S[i]] = [i]

    #計算
    ans = 0
    for i in range(N+1):
        if K + S[i] in D:
            ans += len(D[K + S[i]])
    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #累積和
    Sum = [0]
    for i in range(N):
        Sum.append(Sum[i]+A[i])
    #累積和の差がKになる組み合わせを数える
    from collections import Counter
    c = Counter(Sum)
    ans = 0
    for i in c:
        if i + K in c:
            ans += c[i] * c[i+K]
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A[64])
    #print(A[

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N,K,A)
    #print("A =",A)
    #print("K =",K)
    #print("N =",N)
    
    # 累積和を求める
    s = [0]
    for i in range(N):
        s.append(s[i] + A[i])
    #print("s =",s)
    
    # 累積和の差分を求める
    d = {}
    for i in range(N+1):
        #print("s[i] =",s[i])
        #print("K =",K)
        #print("s[i]-K =",s[i]-K)
        if s[i]-K in d:
            d[s[i]-K] += 1
        else:
            d[s[i]-K] = 1
    #print("d =",d)
    
    # 答えを求める
    ans = 0
    for i in range(N+1):
        #print("d[s[i]] =",d[s[i]])
        ans += d[s[i]]
        #print("ans =",ans)
    print(ans)
