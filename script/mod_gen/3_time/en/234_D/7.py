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

if __name__ == '__main__':
    main()