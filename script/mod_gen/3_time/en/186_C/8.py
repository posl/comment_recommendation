def is_valid(n):
    if '7' in str(n):
        return False
    if '7' in oct(n):
        return False
    return True

if __name__ == '__main__':
    is_valid()