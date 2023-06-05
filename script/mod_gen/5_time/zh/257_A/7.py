def getNthChar(n, x):
    if n == 1:
        return chr(ord('A') + x - 1)
    else:
        return chr(ord('A') + x - 1 + (n - 1) * 26)

if __name__ == '__main__':
    getNthChar()