def find_missing_number(n, a):
    a.sort()
    for i in range(1, n):
        if a[i] != i:
            return i
    return n

if __name__ == '__main__':
    find_missing_number()