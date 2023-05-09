def lunlun(n):
    if n < 10:
        return n
    last_digit = n % 10
    if last_digit == 0:
        return lunlun(n - 1)
    elif last_digit == 9:
        return lunlun(n + 1)
    else:
        return lunlun(n - 1) if last_digit > n // 10 % 10 else lunlun(n + 1)
print(lunlun(int(input())))

if __name__ == '__main__':
    lunlun()