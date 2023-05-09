def print_tile(n, a, b):
    for i in range(a):
        for j in range(n):
            if (i + j) % 2 == 0:
                print('.' * b, end='')
            else:
                print('#' * b, end='')
        print()

if __name__ == '__main__':
    print_tile()