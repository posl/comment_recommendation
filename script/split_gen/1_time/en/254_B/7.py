def print_pascal(n):
    if n == 1:
        print(1)
    else:
        print_pascal(n - 1)
        for i in range(n):
            if i == 0 or i == n - 1:
                print(1, end=' ')
            else:
                print(1, end=' ')
                for j in range(1, i):
                    print(1, end=' ')
                print(1, end=' ')
        print()
