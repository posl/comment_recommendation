def test():
    N = input()
    N = int(N)
    if N < 0 or N > 9999:
        return
    print("%04d" % N)

if __name__ == '__main__':
    test()