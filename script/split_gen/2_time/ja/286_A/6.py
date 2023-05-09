def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    # 1. P-QとR-Sを入れ替える
    # 2. P-RとQ-Sを入れ替える
    # 3. P-SとQ-Rを入れ替える
    # という操作を行う
    # つまり、PとQを入れ替えた後、QとRを入れ替えた後、RとSを入れ替えた後、PとSを入れ替える
    # これで、P-QとR-Sが入れ替わる
    # これを、P-QとR-Sが入れ替わるまで繰り返す
    while P < Q and R < S:
        # 1
        for i in range(P-1, Q-1):
            A[i], A[i+1] = A[i+1], A[i]
        # 2
        for i in range(Q-1, R-1):
            A[i], A[i+1] = A[i+1], A[i]
        # 3
        for i in range(R-1, S-1):
            A[i], A[i+1] = A[i+1], A[i]
        # 4
        for i in range(P-1, S-1):
            A[i], A[i+1] = A[i+1], A[i]
    print(*A)
