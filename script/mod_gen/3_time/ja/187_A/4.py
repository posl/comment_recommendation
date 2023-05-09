def sum_digit(num):
    s = str(num)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum

if __name__ == '__main__':
    sum_digit()