def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
