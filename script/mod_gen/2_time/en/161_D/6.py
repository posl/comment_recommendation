def lunlun(n):
    if n < 10:
        return [n]
    else:
        return [int(str(n)[0]) * 10 ** (len(str(n)) - 1) + i for i in lunlun(n % 10 ** (len(str(n)) - 1)) if abs(int(str(n)[0]) - i) <= 1]

if __name__ == '__main__':
    lunlun()