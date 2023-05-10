def round_number(number):
    if number >= 0.5:
        return int(number) + 1
    else:
        return int(number)

if __name__ == '__main__':
    round_number()