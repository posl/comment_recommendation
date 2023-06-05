def min_diff(S):
    min_diff = 999
    for i in range(len(S)-2):
        x = int(S[i:i+3])
        diff = abs(753 - x)
        if diff < min_diff:
            min_diff = diff
    return min_diff
