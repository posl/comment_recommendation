def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True
S = input()

if __name__ == '__main__':
    is_int()