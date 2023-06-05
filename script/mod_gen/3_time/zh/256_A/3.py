def pow2(n):
    if n == 0:
        return 1
    else:
        return 2 * pow2(n-1)

if __name__ == '__main__':
    pow2()