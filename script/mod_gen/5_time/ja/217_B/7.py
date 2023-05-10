def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    if 'ABC' not in S:
        print('ABC')
    elif 'ARC' not in S:
        print('ARC')
    elif 'AGC' not in S:
        print('AGC')
    elif 'AHC' not in S:
        print('AHC')
    else:
        print('Error')

if __name__ == '__main__':
    main()