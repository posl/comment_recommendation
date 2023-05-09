def jog(A, B, C, D, E, F, X):
    # 高橋君の距離
    T = (A + C) * (X // (A + C)) + min(A, X % (A + C))
    # 青木君の距離
    A = (D + F) * (X // (D + F)) + min(D, X % (D + F))
    # 高橋君の方が長い
    if T * E > A * B:
        print("Takahashi")
    # 青木君の方が長い
    elif T * E < A * B:
        print("Aoki")
    # 同じ
    else:
        print("Draw")
