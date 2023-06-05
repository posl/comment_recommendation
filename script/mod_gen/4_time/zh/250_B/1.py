def print_tile(a, b):
    for i in range(a):
        for j in range(b):
            if (i + j) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    print_tile()