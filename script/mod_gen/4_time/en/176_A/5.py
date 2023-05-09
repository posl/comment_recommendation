def takoyaki():
    # read in input
    n, x, t = map(int, input().split())
    # print(n, x, t)
    # find number of times x fits into n
    # print(n // x)
    # find remainder
    # print(n % x)
    # if remainder is 0, then we are done
    # if remainder is not 0, then we need to add 1 to n // x
    # return n // x * t
    return ((n // x) + (1 if n % x else 0)) * t
print(takoyaki())

if __name__ == '__main__':
    takoyaki()