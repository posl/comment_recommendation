def main():
    N = int(input())
    print('1')
    if N > 1:
        print('1 1')
    if N > 2:
        for i in range(1, N-1):
            print('1', end='')
            for j in range(1, i):
                print(' ' + str(int((i-1)*(i-2)/2 + j)), end='')
            print(' 1')

if __name__ == '__main__':
    main()