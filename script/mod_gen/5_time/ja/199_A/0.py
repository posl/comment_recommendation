def main():
    # input
    A, B, C = map(int, input().split())
    # compute
    # output
    if A**2 + B**2 < C**2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()