def getNthCharOfConcatenatedString(N, X):
    return chr(ord('A') + (X - 1) % 26)

if __name__ == '__main__':
    getNthCharOfConcatenatedString()