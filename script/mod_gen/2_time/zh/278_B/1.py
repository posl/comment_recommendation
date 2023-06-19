def check_time(h, m):
    if h > 23 or h < 0 or m > 59 or m < 0:
        return False
    else:
        return True

if __name__ == '__main__':
    check_time()