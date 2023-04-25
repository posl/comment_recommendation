Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N):
        if P[i - K] < P[i]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    for i in range(K, N):
        print(P[i - K])
    for i in range(K):
        print(P[N - K])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    Q = [P[i] for i in range(K)]
    Q.sort()
    print(Q[K-1])
    for i in range(K, N):
        if P[i] <= Q[0]:
            continue
        for j in range(K):
            if P[i] <= Q[j]:
                Q.insert(j, P[i])
                Q.pop(0)
                break
        print(Q[K-1])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = sorted(P)
    for i in range(K, N):
        print(P[i - K])

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N):
        print(max(P[i-K:i+1]))

main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    ans = []
    for i in range(K, N):
        if P[i] > max(P[i - K:i]):
            ans.append('Yes')
        else:
            ans.append('No')
    print('

'.join(ans))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]

    # 1-indexed
    bit = BinaryIndexedTree(N)

    # P[i]より小さい値の個数を求める
    # P[i]より小さい値の個数がK未満ならば、P[i]はK番目に大きい値である
    ans = []
    for i in range(N):
        bit.add(P[i], 1)
        if i >= K - 1:
            if i >= K:
                bit.add(P[i - K], -1)
            left, right = 0, N
            while right - left > 1:
                mid = (left + right) // 2
                if bit.sum(mid) < K:
                    left = mid
                else:
                    right = mid
            ans.append(str(right))

    print('

'.join(ans))

=======
Suggestion 8

def main():
    #入力を受け取る
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    #K番目の最大値を求める
    #k番目の最大値は、Pのk番目の値を最大値として、それより小さい値を含む区間の最大値となる
    #区間の最大値は、セグ木で管理する
    #k番目の最大値は、k-1番目の最大値と比較して、大きければ、k-1番目の最大値を、小さければ、k番目の最大値を出力する
    #セグ木の初期化
    seg = [0]*(2*N)
    #セグ木の値を更新する
    def update(k,x):
        k += N
        seg[k] = x
        while k > 1:
            k //= 2
            seg[k] = max(seg[k*2],seg[k*2+1])
    #セグ木の値を取得する
    def query(a,b,k,l,r):
        if r <= a or b <= l:
            return 0
        if a <= l and r <= b:
            return seg[k]
        vl = query(a,b,k*2,l,(l+r)//2)
        vr = query(a,b,k*2+1,(l+r)//2,r)
        return max(vl,vr)
    #セグ木の初期化
    for i in range(N):
        update(i,P[i])
    #K番目の最大値を求める
    ans = []
    ans.append(query(0,K,1,0,N))
    for i in range(K,N):
        if P[i-K] == ans[-1]:
            ans.append(query(0,i+1,1,0,N))
        else:
            ans.append(max(ans[-1],P[i]))
    #出力
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #P[i]のK番目に大きい値を求める
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか？
    #P[i]のK番目に大きい値は、P[i]より小さい値のうち、K個以上あるか

=======
Suggestion 10

def get_kth_greatest_value(n,k,p):
    p = p[:k] # p[0:k]
    p.sort(reverse=True)
    print(p[0])
    for i in range(k,n):
        if p[0] < p[i]:
            p[0] = p[i]
            p.sort(reverse=True)
        print(p[0])
