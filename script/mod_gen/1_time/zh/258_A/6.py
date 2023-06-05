def problem258_a():
    k = int(input())
    h = k//60
    m = k%60
    print("{:02d}:{:02d}".format(21+h,m))

if __name__ == '__main__':
    problem258_a()