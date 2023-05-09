def calc(h,a):
    if h % a == 0:
        return h // a
    else:
        return h // a + 1

if __name__ == '__main__':
    calc()