def print_char(n, x):
    if n == 1:
        print(chr(ord('A') + x - 1))
    else:
        print_char(n - 1, x - 1)
        print(chr(ord('A') + x - 1))
        print_char(n - 1, x - 1)
n, x = map(int, input().split())
print_char(n, x)
