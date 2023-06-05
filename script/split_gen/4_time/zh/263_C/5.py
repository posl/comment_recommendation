def print_all_sequence(n, m):
    if n == 0:
        print()
    else:
        for i in range(1, m + 1):
            print(i, end=' ')
            print_all_sequence(n - 1, i - 1)
            print()
