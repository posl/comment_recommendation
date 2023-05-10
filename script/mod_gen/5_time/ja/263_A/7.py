def main():
    # input
    A, B, C, D, E = map(int, input().split())
    # compute
    # output
    if A==B and A==C and D==E:
        print('Yes')
    elif A==B and C==D and C==E:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()