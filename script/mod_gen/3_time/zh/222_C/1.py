def compare(a,b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return -1
        else:
            return 1
    else:
        return 1

if __name__ == '__main__':
    compare()