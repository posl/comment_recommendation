def find_missing_number(s):
    s = list(s)
    s = [int(i) for i in s]
    s.sort()
    for i in range(10):
        if i not in s:
            return i
    return -1

if __name__ == '__main__':
    find_missing_number()