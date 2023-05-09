def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    A.insert(0, 0)
    if M == 0:
        print(1)
        exit()
    # 空白の長さをリスト化
    S = []
    for i in range(M+1):
        if A[i+1] - A[i] - 1 != 0:
            S.append(A[i+1] - A[i] - 1)
    # 空白の長さの最大値を求める
    maxS = max(S)
    # 空白の長さが最大値の場合のスタンプの幅を求める
    K = []
    for i in range(M+1):
        if A[i+1] - A[i] - 1 == maxS:
            K.append(A[i+1] - A[i] - 1)
            break
        elif A[i+1] - A[i] - 1 == maxS - 1:
            K.append(A[i+1] - A[i] - 1)
        elif A[i+1] - A[i] - 1 == maxS - 2:
            K.append(A[i+1] - A[i] - 1)
    if len(K) == 1:
        print(maxS)
    else:
        print(maxS - 1)
