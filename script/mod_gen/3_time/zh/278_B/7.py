def is_valid_time(h,m):
    if h < 0 or h > 23 or m < 0 or m > 59:
        return False
    else:
        return True

if __name__ == '__main__':
    is_valid_time()