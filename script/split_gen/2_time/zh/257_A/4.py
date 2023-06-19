def problem257_a():
    n, x = [int(i) for i in input().split()]
    print(chr(ord('A') + x // n - 1), end='')
