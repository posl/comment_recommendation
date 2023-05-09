def lunlun(n):
    if n < 10:
        return n
    else:
        return lunlun(n // 10) * 10 + n % 10

if __name__ == '__main__':
    lunlun()