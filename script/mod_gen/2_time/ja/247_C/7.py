def print_seq(n):
    if n == 1:
        print(1, end=" ")
        return
    print_seq(n-1)
    print(n, end=" ")
    print_seq(n-1)
