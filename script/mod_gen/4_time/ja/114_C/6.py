def is753(n):
    if n < 100:
        return False
    else:
        s = str(n)
        if '7' in s and '5' in s and '3' in s:
            return True
        else:
            return False

if __name__ == '__main__':
    is753()