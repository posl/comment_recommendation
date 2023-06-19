def get_hex(n):
    if n < 10:
        return str(n)
    else:
        return chr(ord('A') + n - 10)
