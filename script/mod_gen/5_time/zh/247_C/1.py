def print_seq(n):
    if n == 1:
        print(1)
        return
    print_seq(n-1)
    print(n)
    print_seq(n-1)
