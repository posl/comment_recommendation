Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    print(sum([sum(A[i]) for i in range(H)]) - H * W * min([min(A[i]) for i in range(H)]))

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    print(sum([min(a[i]) for i in range(h)]) * w - sum([sum(a[i]) for i in range(h)]))

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [min(a[i]) for i in range(h)]
    c = [min([a[i][j] for i in range(h)]) for j in range(w)]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += max(a[i][j] - b[i] - c[j], 0)
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # Aの各要素の最小値を求める
    min_A = min([min(A[i]) for i in range(H)])

    # Aの各要素からmin_Aを引いた値をsum_Aに足していく
    sum_A = 0
    for i in range(H):
        for j in range(W):
            sum_A += A[i][j] - min_A

    print(sum_A)

=======
Suggestion 5

def main():
    #入力
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]

    #Aの合計値を求める
    A_sum = sum([sum(A[i]) for i in range(H)])

    #Aの合計値をH*Wで割った値を求める
    A_avg = A_sum // (H * W)

    #Aの合計値をH*Wで割った余りを求める
    A_mod = A_sum % (H * W)

    #Aの合計値をH*Wで割った余りが0でない場合、A_avgを1増やす
    if A_mod != 0:
        A_avg += 1

    #Aの合計値をH*Wで割った値をA_avgとしたときの、Aの合計値との差を求める
    A_diff = [abs(A_avg - A[i][j]) for i in range(H) for j in range(W)]

    #Aの合計値をH*Wで割った値をA_avgとしたときの、Aの合計値との差の合計値を求める
    A_diff_sum = sum(A_diff)

    #Aの合計値をH*Wで割った値をA_avgとしたときの、Aの合計値との差の合計値を2で割った値を出力する
    print(A_diff_sum // 2)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    #print(H, W)
    #print(A)
    min = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    #print(min)
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min
    print(ans)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [A_i for A_i in A for _ in range(W)]
    print(sum([min(A_i) for A_i in A]))

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    #print(A)

    # 全てのマスの合計値の平均を求める
    sum = 0
    for i in range(H):
        for j in range(W):
            sum += A[i][j]
    ave = sum / (H * W)
    #print(ave)

    # 全てのマスの合計値の平均を超えないようにブロックを取り除く
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] > ave:
                ans += A[i][j] - ave
    print(int(ans))

=======
Suggestion 9

def main():
    #入力
    H,W = map(int,input().split())
    #print(H,W)
    A = [list(map(int,input().split())) for _ in range(H)]
    #print(A)
    #最小値を求める
    min_A = min([min(A[i]) for i in range(H)])
    #print(min_A)
    #最小値を引いた値を出力
    print(sum([sum([A[i][j]-min_A for j in range(W)]) for i in range(H)]))

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]

    # 1. Aの中の最小値を求める
    # 2. 最小値を引く
    # 3. Aの中の最小値を求める
    # 4. 2.と3.を繰り返す
    # 5. 繰り返しの回数を出力する

    # 1. Aの中の最小値を求める
    min_A = min([min(A[i]) for i in range(H)])

    # 2. 最小値を引く
    for i in range(H):
        for j in range(W):
            A[i][j] -= min_A

    # 3. Aの中の最小値を求める
    min_A = min([min(A[i]) for i in range(H)])

    # 4. 2.と3.を繰り返す
    while min_A != 0:
        # 2. 最小値を引く
        for i in range(H):
            for j in range(W):
                A[i][j] -= min_A

        # 3. Aの中の最小値を求める
        min_A = min([min(A[i]) for i in range(H)])

    # 5. 繰り返しの回数を出力する
    print(min_A)
