Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #N個の箱が左右一列に並んでおり、左からi番目の箱にはAi個のお菓子が入っています。
    #あなたは、連続したいくつかの箱からお菓子を取り出してM人の子供たちに均等に配りたいと考えています。
    #そこで、以下を満たす組(l,r)の総数を求めてください。
    #l,rはともに整数であり1≦l≦r≦Nを満たす
    #Al+Al+1+...+ArはMの倍数である
    N,M=list(map(int,input().split()))
    A=list(map(int,input().split()))
    #print(N,M,A)
    #print(sum(A))
    #print(sum(A)%M)
    #print(sum(A)//M)
    #print(sum(A)//M+1)
    #print(sum(A)//M+2)
    #print(sum(A)//M+3)
    #print(sum(A)//M+4)
    #print(sum(A)//M+5)
    #print(sum(A)//M+6)
    #print(sum(A)//M+7)
    #print(sum(A)//M+8)
    #print(sum(A)//M+9)
    #print(sum(A)//M+10)
    #print(sum(A)//M+11)
    #print(sum(A)//M+12)
    #print(sum(A)//M+13)
    #print(sum(A)//M+14)
    #print(sum(A)//M+15)
    #print(sum(A)//M+16)
    #print(sum(A)//M+17)
    #print(sum(A)//M+18)
    #print(sum(A)//M+19)
    #print(sum(A)//M+20)
    #print(sum(A)//M+21)
    #print(sum(A)//M+22)
    #print(sum(A)//M+23)
    #print(sum(A)//M+24)
    #print(sum(A)//M+25)
    #print(sum(A)//M+26)
    #print(sum(A)//M+27)
    #print(sum(A)//M+28)
    #print

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]

    ans = 0
    cnt = [0] * M
    for i in range(N + 1):
        ans += cnt[sum_A[i] % M]
        cnt[sum_A[i] % M] += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])

    # 累積和の剰余
    R = [s % M for s in S]

    # 剰余の個数
    cnt = {}
    for r in R:
        if r in cnt:
            cnt[r] += 1
        else:
            cnt[r] = 1

    # 組み合わせの数
    ans = 0
    for c in cnt.values():
        ans += c * (c - 1) // 2

    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 累積和
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    # 余りの個数を数える
    cnt = [0] * m
    for i in range(n + 1):
        cnt[s[i] % m] += 1
    # 組の数を数える
    ans = 0
    for i in range(m):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    B = [0]
    for i in range(N):
        B.append(B[i] + A[i])
    # 累積和の値を M で割った余りを計算
    C = [b % M for b in B]
    # 余りの個数を数える
    D = [0] * M
    for c in C:
        D[c] += 1
    # 余りの個数を数える
    ans = 0
    for d in D:
        ans += d * (d - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A.insert(0, 0)
    for i in range(1, N+1):
        A[i] = (A[i] + A[i-1]) % M
    from collections import Counter
    cnt = Counter(A)
    ans = 0
    for k, v in cnt.items():
        ans += v * (v-1) // 2
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # Sのmod Mでの累積和
    SS = [0] * (N + 1)
    for i in range(N + 1):
        SS[i] = S[i] % M
    # SSの各要素の個数
    SS_cnt = [0] * M
    for i in range(N + 1):
        SS_cnt[SS[i]] += 1
    # SSの各要素の個数から組み合わせを計算
    ans = 0
    for i in range(M):
        ans += SS_cnt[i] * (SS_cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))

    #累積和を求める
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]

    #S[i]をMで割った余りを求める
    R = [0]*(N+1)
    for i in range(N+1):
        R[i] = S[i] % M

    #Rの値ごとに出現回数を求める
    from collections import Counter
    C = Counter(R)

    #Rの値ごとに出現回数を求める
    ans = 0
    for v,c in C.items():
        ans += c*(c-1)//2

    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和のリスト
    sum_list = [0]
    for i in range(N):
        sum_list.append(sum_list[i] + A[i])
    
    # 各余りの数
    remainders = [0] * M
    for i in range(N+1):
        remainders[sum_list[i] % M] += 1

    # 組み合わせ
    ans = 0
    for i in range(M):
        ans += remainders[i] * (remainders[i] - 1) // 2

    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    #print(len(A))

    #Aの累積和を求める
    for i in range(1, len(A)):
        A[i] += A[i-1]
    #print(A)

    #Aの累積和をMで割った余りを求める
    for i in range(len(A)):
        A[i] %= M
    #print(A)

    #Aの累積和をMで割った余りの出現回数を求める
    #Aの累積和をMで割った余りが0の場合、1回出現する
    #Aの累積和をMで割った余りが1の場合、2回出現する
    #Aの累積和をMで割った余りが2の場合、3回出現する
    #...
    #Aの累積和をMで割った余りがM-1の場合、M回出現する
    #Aの累積和をMで割った余りがMの場合、1回出現する
    #Aの累積和をMで割った余りがM+1の場合、2回出現する
    #...
    #Aの累積和をMで割った余りが2M-1の場合、M+1回出現する
    #Aの累積和をMで割った余りが2Mの場合、1回出現する
    #Aの累積和をMで割った余りが2M+1の場合、2回出現する
    #...
    #Aの累積和をMで割った余りが3M-1の場合、M+2回出現する
    #Aの累積
