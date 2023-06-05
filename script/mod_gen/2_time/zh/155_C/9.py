def check_evenly_divisible(number):
    if number % 3 == 0 or number % 5 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    check_evenly_divisible()