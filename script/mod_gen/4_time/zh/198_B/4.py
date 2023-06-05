def is_huiwen(number):
    number = str(number)
    for i in range(len(number)):
        if number[i] != number[-(i+1)]:
            return False
    return True

if __name__ == '__main__':
    is_huiwen()