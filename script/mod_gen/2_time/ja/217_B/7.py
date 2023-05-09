def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if 'ABC' in s:
        s.remove('ABC')
    if 'ARC' in s:
        s.remove('ARC')
    if 'AGC' in s:
        s.remove('AGC')
    if 'AHC' in s:
        s.remove('AHC')
    print(s[0])

if __name__ == '__main__':
    main()