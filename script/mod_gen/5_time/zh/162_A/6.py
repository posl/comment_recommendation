def isSeven(n):
    if n % 10 == 7 or (n // 10) % 10 == 7 or n // 100 == 7:
        return True
    else:
        return False

if __name__ == '__main__':
    isSeven()