def is_permutation(numbers):
    numbers.sort()
    for index, number in enumerate(numbers):
        if index+1 != number:
            return False
    return True

if __name__ == '__main__':
    is_permutation()