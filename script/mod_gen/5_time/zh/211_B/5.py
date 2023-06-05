def main():
    #input
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    #compute
    s = [s1,s2,s3,s4]
    if 'H' in s and '2B' in s and '3B' in s and 'HR' in s:
        print('Yes')
    else:
        print('No')
    #output

if __name__ == '__main__':
    main()