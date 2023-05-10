def is753(num):
    if num == 0:
        return False
    if num % 10 == 7 or num % 10 == 5 or num % 10 == 3:
        return True
    return is753(num // 10)

if __name__ == '__main__':
    is753()