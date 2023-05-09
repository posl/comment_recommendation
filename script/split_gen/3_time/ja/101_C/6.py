def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 最小値を求める
    minA = min(A)
    # 最小値を1にする
    for i in range(N):
        A[i] = A[i] - minA + 1
    # 1~Nまでの値をカウントするリストを作成
    B = [0 for i in range(N)]
    for i in range(N):
        B[A[i]-1] += 1
    # K個以上の値がある場合は、K個になるようにする
    for i in range(N):
        if B[i] >= K:
            B[i] = K
    # 1~Nまでの値をカウントするリストを作成
    C = [0 for i in range(N)]
    for i in range(N):
        C[A[i]-1] += 1
    # K個以上の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] >= K:
            C[i] = K
    # K個未満の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] < K:
            C[i] = 0
    # K個未満の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] < K:
            C[i] = 0
    # K個未満の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] < K:
            C[i] = 0
    # K個未満の値がある場合は、K個になるようにする
    for i in range(N):
        if C[i] < K:
            C[i] = 0
    # K個未満の値がある場合
