def calc_divisible_count(numbers, div):
    count = 0
    sum = 0
    remainder_dict = {}
    for number in numbers:
        sum += number
        remainder = sum % div
        if remainder == 0:
            count += 1
        if remainder in remainder_dict:
            remainder_dict[remainder] += 1
        else:
            remainder_dict[remainder] = 1
    for remainder in remainder_dict:
        count += remainder_dict[remainder] * (remainder_dict[remainder] - 1) // 2
    return count

if __name__ == '__main__':
    calc_divisible_count()