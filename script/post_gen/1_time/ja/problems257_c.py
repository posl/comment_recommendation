Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
    for i in range(N):
        if S[i] == '1':
            ans += 1
        else:
            ans -= 1
        ans = max(ans, 0)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i] == S[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # 体重でソート
    W, S = zip(*sorted(zip(W, S)))
    # 体重の累積和
    W_sum = [0]
    for i in range(N):
        W_sum.append(W_sum[i] + W[i])
    # 体重の累積和が体重の累積和の最大値から体重の累積和の最小値を引いたもの
    W_sum_max = W_sum[-1]
    W_sum_min = W_sum[0]
    # 体重の累積和の最大値から体重の累積和の最小値を引いたものの半分
    W_sum_half = (W_sum_max - W_sum_min) / 2
    # 体重の累積和の最大値から体重の累積和の最小値を引いたものの半分を超える体重の累積和の最小値
    W_sum_half_max = W_sum_min + W_sum_half
    # 体重の累積和の最大値から体重の累積和の最小値を引いたものの半分を下回る体重の累積和の最大値
    W_sum_half_min = W_sum_max - W_sum_half
    # 体重の累積和が体重の累積和の最大値から体重の累積和の最小値を引いたものの半分を超える体重の累積和の最小値を超える体重の累積和の最大値
    W_sum_half_max_max = W_sum_half_max + W_sum_half
    # 体重の累積和が体重の累積和の最大値から体重の累積和の最小値を引いたものの

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N, S, W)
    #print(type(N), type(S), type(W))
    #print(len(S))

    #S = "10101"
    #W = [60, 45, 30, 40, 80]
    #N = 5

    #S = "000"
    #W = [1, 2, 3]
    #N = 3

    #S = "10101"
    #W = [60, 50, 50, 50, 60]

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    W = list(map(int,input().split()))

    # 体重の降順に並び替え
    W = sorted(W,reverse=True)
    #print(W)

    # 体重の降順に並び替えたときの、Sの0と1の数をカウント
    # 0の数が0のとき、すべての人が大人
    # 0の数がNのとき、すべての人が子供
    # 0の数がN/2のとき、体重の降順で半分が子供、半分が大人
    # 0の数がN/2+1のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+2のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+3のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+4のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+5のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+6のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+7のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+8のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+9のとき、体重の降順で

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))

    # Sの0と1の数をカウント
    S0 = S.count('0')
    S1 = S.count('1')

    # Wをソート
    W.sort()

    # Wの累積和を計算
    Wsum = [0] * (N + 1)
    for i in range(N):
        Wsum[i + 1] = Wsum[i] + W[i]

    # 二分探索
    def is_ok(x):
        # x未満の人の体重の和
        w0 = Wsum[S0]
        # x以上の人の体重の和
        w1 = Wsum[-1] - Wsum[N - S1]
        # 残りの人の体重の和
        w2 = Wsum[N] - w0 - w1
        # 二つの体重の和の差がx未満ならTrue
        return abs(w2 - w0) < x

    # 二分探索
    def binary_search():
        # 求める範囲を[l, r]とする
        l = 0
        r = 10 ** 9
        while r - l > 1:
            x = (l + r) // 2
            if is_ok(x):
                l = x
            else:
                r = x
        return l

    # 二分探索
    ans = binary_search()
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # 人の体重の最大値
    maxW = max(W)
    # 人の体重の最小値
    minW = min(W)
    # 体重の最大値と最小値を使って、体重の増減の幅を決める
    dW = maxW - minW
    # 体重の増減の幅の最大値
    maxdW = 10**9
    # 体重の増減の幅の最小値
    mindW = 1
    # 体重の増減の幅の中央値
    midW = (maxdW + mindW) // 2
    # 体重の増減の幅が最大値になるまで繰り返す
    while dW != maxdW:
        # 体重の増減の幅の中央値の値で判定する
        # 体重の増減の幅の中央値が小さいと、体重の増減の幅を大きくする
        if judge(S, W, midW):
            mindW = midW
        # 体重の増減の幅の中央値が大きいと、体重の増減の幅を小さくする
        else:
            maxdW = midW
        # 体重の増減の幅の中央値を更新する
        midW = (maxdW + mindW) // 2
        # 体重の増減の幅の最大値と最小値の差を更新する
        dW = maxdW - mindW
    # 体重の増減の幅の中央値を出力する
    print(midW)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N)
    #print(S)
    #print(W)
    #print("len(S)=",len(S))
    #print("len(W)=",len(W))
    if len(S) != N:
        print("len(S) != N")
    if len(W) != N:
        print("len(W) != N")
    if len(S) != len(W):
        print("len(S) != len(W)")
    #print("S=",S)
    #print("W=",W)
    #print("S[0]=",S[0])
    #print("W[0]=",W[0])
    #print("S[1]=",S[1])
    #print("W[1]=",W[1])
    #print("S[2]=",S[2])
    #print("W[2]=",W[2])
    #print("S[3]=",S[3])
    #print("W[3]=",W[3])
    #print("S[4]=",S[4])
    #print("W[4]=",W[4])
    #print("S[5]=",S[5])
    #print("W[5]=",W[5])
    #print("S[6]=",S[6])
    #print("W[6]=",W[6])
    #print("S[7]=",S[7])
    #print("W[7]=",W[7])
    #print("S[8]=",S[8])
    #print("W[8]=",W[8])
    #print("S[9]=",S[9])
    #print("W[9]=",W[9])
    #print("S[10]=",S[10])
    #print("W[10]=",W[10])
    #print("S[11]=",S[11])
    #print("W[11]=",W[11])
    #print("S[12]=",S[12])
    #print("W[12]=",W[12])
    #print("S[13]=",S[13])
    #print("W[13]=",W[13])
    #print("S[

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    W = list(map(int,input().split()))
    #print(N,S,W)
    #print(S[0])
    #print(W[0])
    #print(W)
    #print(W[0:3])
    #print(W[3:5])

    ans = 0
    for X in range(1,10**9+1):
        #print(X)
        #print(W[0:X])
        #print(W[X:N])
        #print(S[0:X])
        #print(S[X:N])
        #print(W[0:X])
        #print(W[X:N])
        #print(S[0:X])
        #print(S[X:N])
        #print(sum(W[0:X]))
        #print(sum(W[X:N]))
        #print(sum(S[0:X]))
        #print(sum(S[X:N]))
        if sum(W[0:X]) < X*sum(S[0:X]):
            #print("a")
            continue
        if sum(W[X:N]) >= X*sum(S[X:N]):
            #print("b")
            continue
        ans = max(ans,sum(S[0:X])+sum(S[X:N]))
        #print(ans)
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    M = max(W)
    # 体重の最大値を最大のXにする
    X = M
    # 体重の最大値を最小のXにする
    Y = 0
    # XとYの差が1になるまで繰り返す
    while X - Y > 1:
        # XとYの中間値をZにする
        Z = (X + Y) // 2
        # ZをXにする
        X = Z
        # 高橋君が正しく判定できる人数を初期化
        count = 0
        # 体重がZ未満の人が子供であることを判定
        for i in range(N):
            if W[i] < Z and S[i] == '0':
                count += 1
            elif W[i] >= Z and S[i] == '1':
                count += 1
        # 高橋君が正しく判定できる人数がN人未満の場合
        if count < N:
            # ZをYにする
            Y = Z
    # 高橋君が正しく判定できる人数を出力
    print(count)
