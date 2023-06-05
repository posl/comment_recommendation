def get_name(num):
    if num <= 26:
        return chr(num + ord('a') - 1)
    else:
        return get_name((num - 1) // 26) + get_name((num - 1) % 26 + 1)

if __name__ == '__main__':
    get_name()