def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    #ゼロの数
    zero = A.count(0)
    #ゼロを除いたリスト
    A = [a for a in A if a != 0]
    #ゼロがN個ある場合
    if zero == N:
        print(0)
        return
    #ゼロがN個未満ある場合
    if zero > 0:
        #ゼロを含む組み合わせの数
        zero_comb = zero * (N - zero)
        #ゼロを含む組み合わせの数をKから引く
        K -= zero_comb
        #Kが0以下になった場合
        if K <= 0:
            print(0)
            return
    #ゼロがない場合
    #負の数の数
    minus = len([a for a in A if a < 0])
    #負の数の組み合わせの数
    minus_comb = minus * (N - minus)
    #負の数の組み合わせの数をKから引く
    K -= minus_comb
    #Kが0以下になった場合
    if K <= 0:
        #負の数のリストを作る
        minus = [a for a in A if a < 0]
        #絶対値の大きい順に並べる
        minus.sort(key = lambda x: -abs(x))
        #Kが負の数の数以下の場合
        if -K < len(minus):
            #Kの絶対値の数だけ負の数を掛ける
            ans = 1
            for i in range(abs(K)):
                ans *= minus[i]
            print(ans)
            return
        #Kが負の数の数より大きい場合
        else:
            #Kの絶対値から負の数の数を引いた数だけ正の
