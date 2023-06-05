def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    l = [s1,s2,s3,s4]
    if l.count('H') == 1 and l.count('2B') == 1 and l.count('3B') == 1 and l.count('HR') == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()