def get_name(num):
    if num == 0:
        return ''
    return get_name((num - 1) / 26) + chr((num - 1) % 26 + ord('a'))

if __name__ == '__main__':
    get_name()