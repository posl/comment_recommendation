def count_integer(a,b):
    if a <= b and a >= 1 and b <= 100:
        return b - a + 1
    else:
        return 0

if __name__ == '__main__':
    count_integer()