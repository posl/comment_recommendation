def median(a, l, r):
    if (r - l) % 2 == 0:
        return a[(r + l) // 2]
    else:
        return (a[(r + l) // 2] + a[(r + l) // 2 + 1]) / 2

if __name__ == '__main__':
    median()