def main():
    s = input()
    s1 = s[0]
    s2 = s[1]
    s3 = s[2]
    if s1 == s2:
        print(s3)
    elif s1 == s3:
        print(s2)
    elif s2 == s3:
        print(s1)
    else:
        print('-1')

if __name__ == '__main__':
    main()