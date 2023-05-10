def main():
    s1 = input()
    s2 = input()
    print('Yes' if '#' in (s1[0], s1[1], s2[0], s2[1]) else 'No')

if __name__ == '__main__':
    main()