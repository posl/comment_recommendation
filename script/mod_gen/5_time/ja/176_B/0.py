def is_multiple_of_9(str):
    sum = 0
    for i in range(len(str)):
        sum += int(str[i])
    return sum % 9 == 0

if __name__ == '__main__':
    is_multiple_of_9()