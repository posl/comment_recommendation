def sum_digits(num):
    num = str(num)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum
