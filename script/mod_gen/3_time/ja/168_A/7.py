def is_hon(n):
    if n % 10 in [2,4,5,7,9]:
        return True
    else:
        return False

if __name__ == '__main__':
    is_hon()