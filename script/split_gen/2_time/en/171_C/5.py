def num2name(n):
    if n == 1:
        return 'a'
    else:
        return num2name((n - 1) // 26) + chr(ord('a') + (n - 1) % 26)
