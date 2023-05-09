def count_bigger_than_all_previous_numbers(numbers):
    count = 0
    min = numbers[0]
    for number in numbers:
        if number <= min:
            min = number
            count += 1
    return count
