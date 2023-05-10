def get_name(number):
    if number <= 26:
        return chr(ord('a') + number - 1)
    else:
        return get_name(int((number - 1) / 26)) + get_name((number - 1) % 26 + 1)
