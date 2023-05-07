def make_dog_name(number):
    #print(number)
    dog_name = ''
    while number > 0:
        number -= 1
        dog_name = chr(ord('a') + number % 26) + dog_name
        number //= 26
    return dog_name

if __name__ == '__main__':
    make_dog_name()