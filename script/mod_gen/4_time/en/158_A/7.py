def main():
    s = input()
    if s.count('A') == 3 or s.count('B') == 3:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()