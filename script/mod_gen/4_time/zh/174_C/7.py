def f1(k):
    if k == 1:
        return 1
    else:
        return 10*f1(k-1)+1

if __name__ == '__main__':
    f1()