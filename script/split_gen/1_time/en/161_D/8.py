def lunlun(n):
    if n < 10:
        return n
    else:
        return lunlun(n // 10) + n % 10
