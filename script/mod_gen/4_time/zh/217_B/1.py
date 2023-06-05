def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if 'ABC' not in s:
        print('ABC')
    elif 'ARC' not in s:
        print('ARC')
    elif 'AGC' not in s:
        print('AGC')
    elif 'AHC' not in s:
        print('AHC')

if __name__ == '__main__':
    main()