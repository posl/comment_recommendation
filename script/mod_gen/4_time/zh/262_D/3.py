def countAverage(n, a):
    sum = 0
    for i in range(n):
        sum += a[i]
    if sum % n == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    countAverage()