def print_seq(n, m):
    if n == 1:
        for i in range(1, m+1):
            print(i)
    else:
        for i in range(1, m+1):
            print(i)
            print_seq(n-1, i+1)
