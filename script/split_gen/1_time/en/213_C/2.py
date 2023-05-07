def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # サンプル 2 の場合、H と W が大きいため、
    # 配列を作るとメモリエラーになる。
    # そのため、配列を作らずに、
    # ソートした後に、同じ値が連続している数をカウントする。
    # これを用いて、A, B の値を更新する。
    A.sort()
    B.sort()
    A.append(H + 1)
    B.append(W + 1)
    A_cnt = 1
    B_cnt = 1
    for i in range(N):
        if A[i] == A[i + 1]:
            A_cnt += 1
        else:
            A[i] = A_cnt
            A_cnt = 1
        if B[i] == B[i + 1]:
            B_cnt += 1
        else:
            B[i] = B_cnt
            B_cnt = 1
    for i in range(N):
        print(A[i], B[i])
