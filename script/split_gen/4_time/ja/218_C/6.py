def rotate(S):
    return [''.join(x) for x in zip(*S[::-1])]
