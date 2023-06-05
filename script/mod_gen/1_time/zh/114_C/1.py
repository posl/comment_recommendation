def is753(n):
    s = str(n)
    return s.count('7') and s.count('5') and s.count('3')

if __name__ == '__main__':
    is753()