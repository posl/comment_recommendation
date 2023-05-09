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

if __name__ == '__main__':
    main()