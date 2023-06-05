def get_char_from_string(n, x):
    if n == 1:
        return chr(64+x)
    else:
        return chr(64+((x-1)%26)+1)

if __name__ == '__main__':
    get_char_from_string()