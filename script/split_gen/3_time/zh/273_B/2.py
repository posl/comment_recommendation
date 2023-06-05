def my_round(num, n):
    if n == 0:
        return num
    i = 10 ** n
    if num % i == 0:
        return num
    return num + i - num % i
