def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    # print(s1, s2, s3, s4)
    if 'H' in s1 and 'H' in s2 and 'H' in s3 and 'H' in s4:
        if '2B' in s1 and '2B' in s2 and '2B' in s3 and '2B' in s4:
            if '3B' in s1 and '3B' in s2 and '3B' in s3 and '3B' in s4:
                if 'HR' in s1 and 'HR' in s2 and 'HR' in s3 and 'HR' in s4:
                    print('Yes')
                else:
                    print('No')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()