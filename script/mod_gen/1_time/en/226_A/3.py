def round(number):
    if number >= 0:
        if number % 1 >= 0.5:
            return int(number) + 1
        else:
            return int(number)
    else:
        if number % 1 <= -0.5:
            return int(number) - 1
        else:
            return int(number)

if __name__ == '__main__':
    round()