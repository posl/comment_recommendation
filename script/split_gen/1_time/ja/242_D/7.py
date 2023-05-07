def main():
    S = input()
    Q = int(input())
    # S の 1 文字目から i 文字目までの A,B,C の個数を格納する配列
    # A[i] = S[0:i+1] の A の個数
    # B[i] = S[0:i+1] の B の個数
    # C[i] = S[0:i+1] の C の個数
    A = [0] * (len(S) + 1)
    B = [0] * (len(S) + 1)
    C = [0] * (len(S) + 1)
    for i in range(len(S)):
        if S[i] == "A":
            A[i + 1] = A[i] + 1
            B[i + 1] = B[i]
            C[i + 1] = C[i]
        elif S[i] == "B":
            A[i + 1] = A[i]
            B[i + 1] = B[i] + 1
            C[i + 1] = C[i]
        else:
            A[i + 1] = A[i]
            B[i + 1] = B[i]
            C[i + 1] = C[i] + 1
    for _ in range(Q):
        t, k = map(int, input().split())
        # S^{(t)} の先頭から k 文字目を出力
        # S^{(t)} の先頭から k 文字目の A,B,C の個数を求める
        # S^{(t)} の先頭から k 文字目の A,B,C の個数のうち最大のものを出力する
        # この処理を Q 回行う
        a = A[k] + (A[-1] - A[k]) * (t % 3 == 1) + (B[-1] - B[k]) * (t % 3 == 2) + (C[-1] - C[k]) * (t % 3 == 0)
        b = B[k] + (A[-1] - A[k]) * (t % 3 == 2
