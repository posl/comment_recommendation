def min_max(S):
    min = S
    max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < min:
            min = S
        if S > max:
            max = S
    return min, max

if __name__ == '__main__':
    min_max()