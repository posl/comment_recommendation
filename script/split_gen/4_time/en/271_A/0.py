def convert_to_hex(n):
    if n < 10:
        return str(n)
    elif n == 10:
        return 'A'
    elif n == 11:
        return 'B'
    elif n == 12:
        return 'C'
    elif n == 13:
        return 'D'
    elif n == 14:
        return 'E'
    elif n == 15:
        return 'F'
n = int(input())
first_digit = n // 16
second_digit = n % 16
print(convert_to_hex(first_digit) + convert_to_hex(second_digit))
