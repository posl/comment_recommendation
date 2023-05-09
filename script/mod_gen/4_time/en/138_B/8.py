def inverse_sum(numbers):
    sum = 0
    for number in numbers:
        sum += 1/number
    return 1/sum

if __name__ == '__main__':
    inverse_sum()