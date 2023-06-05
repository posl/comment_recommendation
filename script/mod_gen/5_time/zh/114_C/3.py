def is753(n):
    s = str(n)
    return s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0

if __name__ == '__main__':
    is753()