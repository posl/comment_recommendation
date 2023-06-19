def calc_print_pages(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 + 1

if __name__ == '__main__':
    calc_print_pages()