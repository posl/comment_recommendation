def main():
    S = input()
    s1 = S[0]
    s2 = S[1]
    s3 = S[2]
    if s1 == s2 == s3:
        print(1)
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print(3)
    else:
        print(6)

if __name__ == '__main__':
    main()