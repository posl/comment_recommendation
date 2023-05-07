def num_to_name(n):
    if n <= 26:
        return chr(ord('a') + n - 1)
    else:
        return num_to_name((n - 1) // 26) + chr(ord('a') + (n - 1) % 26)
