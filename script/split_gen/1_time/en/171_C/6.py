def getDogName(N):
    if N <= 26:
        return chr(ord('a') + N - 1)
    else:
        return getDogName((N - 1) // 26) + getDogName((N - 1) % 26 + 1)
