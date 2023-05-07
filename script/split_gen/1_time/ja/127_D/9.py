def main():
    # 1行目の入力
    N, M = map(int, input().split())
    # 2行目の入力
    A = list(map(int, input().split()))
    # 3行目以降の入力
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    # Aの各要素を大きい順に並べる
    A.sort(reverse=True)
    # Cの各要素を大きい順に並べる
    C.sort(reverse=True)
    # Aの各要素を順番に見ていく
    for i in range(N):
        # A[i]の値がCの最大値より小さければ終了
        if A[i] < C[0]:
            break
        # A[i]の値がCの最大値以上で、Bの最大値が0なら終了
        if B[0] == 0:
            break
        # A[i]の値がCの最大値以上で、Bの最大値が0でないなら、A[i]の値をCの最大値に書き換える
        A[i] = C[0]
        # Bの最大値を1減らす
        B[0] -= 1
        # Bの最大値が0になったら、Bの最大値をBの最大値-1の値に書き換える
        if B[0] == 0:
            B.sort(reverse=True)
        # Cの最大値をCの最大値-1の値に書き換える
        C.sort(reverse=True)
    # Aの各要素の合計を求める
    ans = sum(A)
    # 答えを出力
    print(ans)
