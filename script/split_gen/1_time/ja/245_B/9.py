def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 0 から 2000 までの配列を作る
    # 0 は使わない
    # 0 を使わないのは、A に 0 が含まれるかどうかで
    # 答えが変わるから
    B = [0] * 2001
    # A の要素に対応する B の要素に 1 を入れる
    for i in range(N):
        B[A[i]] = 1
    # B の要素が 0 のインデックスを出力する
    # 0 は使わないので、インデックスを 1 ずつずらす
    print(B.index(0))
