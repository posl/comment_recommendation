def base_2(n):
    if n == 0:
        return 0
    else:
        return base_2(n//(-2)) + str(n%(-2))

if __name__ == '__main__':
    base_2()