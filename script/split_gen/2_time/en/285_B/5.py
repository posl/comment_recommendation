def max_non_negative_integer(S, i):
    l = 0
    for j in range(1, len(S)-i+1):
        if S[j-1] != S[j+i-1]:
            l += 1
        else:
            break
    return l
