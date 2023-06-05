def isMultipleOfK(x, k):
    while (x < 0):
        x = x + k
    return (x % k == 0)

if __name__ == '__main__':
    isMultipleOfK()