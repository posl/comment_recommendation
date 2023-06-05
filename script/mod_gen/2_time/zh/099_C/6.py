def withdrawl(n):
    count = 0
    while n > 0:
        if n % 9 == 0:
            n = n - 9
            count = count + 1
        elif n % 6 == 0:
            n = n - 6
            count = count + 1
        elif n % 1 == 0:
            n = n - 1
            count = count + 1
    return count

if __name__ == '__main__':
    withdrawl()