def is_valid_month(month):
    if 0 < int(month) <= 12:
        return True
    else:
        return False

if __name__ == '__main__':
    is_valid_month()