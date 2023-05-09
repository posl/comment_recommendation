def find_divisible_numbers(numbers):
    numbers.sort()
    numbers.reverse()
    divisible_numbers = []
    for i in range(len(numbers)):
        if i == 0:
            divisible_numbers.append(numbers[i])
        else:
            for j in range(len(divisible_numbers)):
                if divisible_numbers[j] % numbers[i] == 0:
                    break
                elif j == len(divisible_numbers) - 1:
                    divisible_numbers.append(numbers[i])
    return divisible_numbers
