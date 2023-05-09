def median(a):
    a = sorted(a)
    return a[(len(a) - 1) // 2]

if __name__ == '__main__':
    median()