def hex(n):
    if n < 0 or n > 255:
        return None
    if n < 16:
        return "0" + hex(n)
    elif n < 256:
        return hex(n // 16) + hex(n % 16)
    else:
        return None
