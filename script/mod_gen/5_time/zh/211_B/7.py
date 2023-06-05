def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 in ['H', '2B', '3B', 'HR'] and s2 in ['H', '2B', '3B', 'HR'] and s3 in ['H', '2B', '3B', 'HR'] and s4 in ['H', '2B', '3B', 'HR']:
        if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
            print('No')
        else:
            print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()