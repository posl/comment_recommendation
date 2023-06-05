def find_first_n(n):
    num = 7
    for i in range(1, n + 1):
        if num % n == 0:
            return i
        num = num * 10 + 7
    return -1

if __name__ == '__main__':
    find_first_n()