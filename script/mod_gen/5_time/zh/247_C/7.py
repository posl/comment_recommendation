def print_seq(n):
    if n == 1:
        return '1'
    else:
        return print_seq(n-1) + ' ' + str(n) + ' ' + print_seq(n-1)

if __name__ == '__main__':
    print_seq()