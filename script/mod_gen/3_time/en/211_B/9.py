def main():
    # Read data
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    # Check data
    if (S1 == 'H' or S2 == 'H' or S3 == 'H' or S4 == 'H') and \
        (S1 == '2B' or S2 == '2B' or S3 == '2B' or S4 == '2B') and \
        (S1 == '3B' or S2 == '3B' or S3 == '3B' or S4 == '3B') and \
        (S1 == 'HR' or S2 == 'HR' or S3 == 'HR' or S4 == 'HR'):
        print('Yes')
    else:
        print('No')
main()
