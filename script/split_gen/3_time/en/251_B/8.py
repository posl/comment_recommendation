def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの要素を0からWまでの範囲に収める
    B = [0] * (W + 1)
    for i in range(N):
        B[A[i]] += 1
    # Bの要素の累積和を取る
    C = [0] * (W + 1)
    for i in range(1, W + 1):
        C[i] = C[i - 1] + B[i]
    # 答えを求める
    ans = 0
    for i in range(W + 1):
        for j in range(i + 1):
            for k in range(j + 1):
                if i + j + k <= W:
                    ans += C[i] * C[j] * C[k]
    print(ans)
