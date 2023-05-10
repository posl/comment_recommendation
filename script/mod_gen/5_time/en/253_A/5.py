def is_median(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False

if __name__ == '__main__':
    is_median()