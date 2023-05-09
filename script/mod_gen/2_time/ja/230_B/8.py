def main():
    s = input()
    if s.count('o') * 2 == len(s):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()