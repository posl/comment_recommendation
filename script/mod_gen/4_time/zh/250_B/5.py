def print_tile(A, B):
    for i in range(A):
        for j in range(B):
            if (i+j)%2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print('')

if __name__ == '__main__':
    print_tile()