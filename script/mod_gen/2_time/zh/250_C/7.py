def print_tile(n,a,b):
    n = int(n)
    a = int(a)
    b = int(b)
    for i in range(a*n):
        for j in range(b*n):
            if ((i//a)+(j//b))%2 == 0:
                print('.',end='')
            else:
                print('#',end='')
        print('')

if __name__ == '__main__':
    print_tile()