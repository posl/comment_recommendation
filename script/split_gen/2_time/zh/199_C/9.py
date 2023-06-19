def process(S, T, A, B):
    if T == 1:
        # S[A-1], S[B-1] = S[B-1], S[A-1]  # 为什么不行？
        S[A-1], S[B-1] = S[B-1], S[A-1]
    elif T == 2:
        S[:len(S)//2], S[len(S)//2:] = S[len(S)//2:], S[:len(S)//2]
    return S
