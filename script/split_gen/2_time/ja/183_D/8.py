def main():
    N, W = map(int, input().split()) #N:人数, W:湯沸かし器の出力
    #S_i:人iが湯沸かし器を使い始める時刻, T_i:人iが湯沸かし器を使い終わる時刻, P_i:人iが1分あたりに使う湯量
    S = [0]*N
    T = [0]*N
    P = [0]*N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())
    
    #1分あたりの湯の使用量を計算
    use = [0]*(2*10**5+1)
    for i in range(N):
        use[S[i]] += P[i]
        use[T[i]] -= P[i]
    
    #累積和を計算
    for i in range(1, 2*10**5+1):
        use[i] += use[i-1]
    
    #湯沸かし器の出力と使用量を比較
    for i in range(2*10**5+1):
        if use[i] > W:
            print("No")
            return
    
    print("Yes")
    return
