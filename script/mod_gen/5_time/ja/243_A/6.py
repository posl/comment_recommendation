def main():
    # input
    V, A, B, C = map(int, input().split())
    # compute
    cnt = 0
    while V > 0:
        V -= A
        cnt += 1
        if V <= 0:
            break
        V -= B
        cnt += 1
        if V <= 0:
            break
        V -= C
        cnt += 1
        if V <= 0:
            break
    # output
    if cnt % 3 == 1:
        print('F')
    elif cnt % 3 == 2:
        print('M')
    elif cnt % 3 == 0:
        print('T')

if __name__ == '__main__':
    main()