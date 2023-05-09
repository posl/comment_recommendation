def calc(a):
    i = 0
    while i < 3:
        a = a[a[i]]
        i += 1
    return a

if __name__ == '__main__':
    calc()