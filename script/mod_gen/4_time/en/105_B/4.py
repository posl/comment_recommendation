def main():
    # input
    N = int(input())
    # compute
    # output
    if N%4 == 0 or N%7 == 0 or N%11 == 0:
        print('Yes')
    elif N%4 == 1 and N >= 9:
        print('Yes')
    elif N%4 == 2 and N >= 18:
        print('Yes')
    elif N%4 == 3 and N >= 7:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()