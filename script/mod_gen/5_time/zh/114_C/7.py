def is753(num):
    if num < 357:
        return False
    if num % 10 == 7:
        return True
    if num % 10 == 5:
        return True
    if num % 10 == 3:
        return True
    return False

if __name__ == '__main__':
    is753()