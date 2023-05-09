def get_str(n):
    if n <= 26:
        return chr(ord('a') + n - 1)
    else:
        return get_str((n - 1) // 26) + chr(ord('a') + (n - 1) % 26)
