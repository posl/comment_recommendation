def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    if S1 == 'H' and S2 == '2B' and S3 == '3B' and S4 == 'HR':
        print('Yes')
    elif S1 == '2B' and S2 == '3B' and S3 == 'HR' and S4 == '3B':
        print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()