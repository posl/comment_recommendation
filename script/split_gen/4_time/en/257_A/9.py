def getNthCharOfConcatenatedString(N, X):
    return chr(ord('A') + (X - 1) % 26)
