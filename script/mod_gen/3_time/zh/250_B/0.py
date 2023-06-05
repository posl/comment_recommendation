def print_tile(n, a, b):
    for i in range(a * n):
        for j in range(b * n):
            if i % 2 == 0:
                if j % 2 == 0:
                    print('.', end='')
                else:
                    print('#', end='')
            else:
                if j % 2 == 0:
                    print('#', end='')
                else:
                    print('.', end='')
        print('')

if __name__ == '__main__':
    print_tile()