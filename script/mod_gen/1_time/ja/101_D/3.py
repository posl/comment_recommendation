def get_num(n):
    if n < 10:
        return n
    else:
        return n % 10 + get_num(n // 10)

if __name__ == '__main__':
    get_num()