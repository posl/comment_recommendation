def min_max(S):
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
    return S_min, S_max

if __name__ == '__main__':
    min_max()