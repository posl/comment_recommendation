def problem271_a(n):
    if n < 0 or n > 255:
        return None
    else:
        return '{:02X}'.format(n)
