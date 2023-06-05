def sum_of_two_numbers(numbers):
    sum = 0
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            sum += numbers[i]*numbers[j]
    return sum

if __name__ == '__main__':
    sum_of_two_numbers()