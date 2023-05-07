def main():
    s1 = input()
    s2 = input()
    print('Yes' if s1[1] == s2[0] and s1[2] == s2[1] and s1[0] == s2[2] else 'No')

if __name__ == '__main__':
    main()