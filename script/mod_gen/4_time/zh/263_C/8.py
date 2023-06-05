def print_list(l):
    print(l[0], end='')
    for i in range(1, len(l)):
        print(' ', end='')
        print(l[i], end='')
    print('')

if __name__ == '__main__':
    print_list()