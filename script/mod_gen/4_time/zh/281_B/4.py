def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    is_num()