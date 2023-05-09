def is_approved(numbers):
    for number in numbers:
        if number % 2 == 0 and number % 3 != 0 and number % 5 != 0:
            return False
    return True

if __name__ == '__main__':
    is_approved()