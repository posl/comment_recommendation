def main():
    # 入力
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    # 出力
    print(solve(N, K, L, R))
