def print_all_strictly_increasing_integer_sequences(n, m):
    if n == 0:
        print()
    else:
        for i in range(1, m+1):
            print(i, end=' ')
            print_all_strictly_increasing_integer_sequences(n-1, m)
            print()
