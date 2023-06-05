def is753(n):
    s = str(n)
    if s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is753()