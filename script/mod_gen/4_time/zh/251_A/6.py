def get_repeat_string(s):
    if len(s) == 1:
        return s * 6
    elif len(s) == 2:
        return s * 3
    else:
        return s * 2

if __name__ == '__main__':
    get_repeat_string()