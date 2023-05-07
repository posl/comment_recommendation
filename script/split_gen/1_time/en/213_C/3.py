def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # ここから書きましょう
    C = [0] * N
    D = [0] * N
    # ここまで書きましょう
    for i in range(N):
        print(C[i], D[i])
