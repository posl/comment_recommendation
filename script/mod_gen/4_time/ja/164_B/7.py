def main():
    # input
    A, B, C, D = map(int, input().split())
    # compute
    # output
    if C <= 0:
        print('No')
    else:
        if A % D == 0:
            if C % B == 0:
                if (A // D) >= (C // B):
                    print('Yes')
                else:
                    print('No')
            else:
                if (A // D) >= (C // B + 1):
                    print('Yes')
                else:
                    print('No')
        else:
            if C % B == 0:
                if (A // D + 1) >= (C // B):
                    print('Yes')
                else:
                    print('No')
            else:
                if (A // D + 1) >= (C // B + 1):
                    print('Yes')
                else:
                    print('No')

if __name__ == '__main__':
    main()