def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == 'HR' or s2 == 'HR' or s3 == 'HR' or s4 == 'HR':
        if s1 == '2B' or s2 == '2B' or s3 == '2B' or s4 == '2B':
            if s1 == '3B' or s2 == '3B' or s3 == '3B' or s4 == '3B':
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()