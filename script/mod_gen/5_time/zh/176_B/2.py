def is_multiple_of_nine(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum % 9 == 0

if __name__ == '__main__':
    is_multiple_of_nine()