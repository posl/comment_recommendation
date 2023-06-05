def getNums(n):
    num = 0
    while n:
        n &= n - 1
        num += 1
    return num

if __name__ == '__main__':
    getNums()