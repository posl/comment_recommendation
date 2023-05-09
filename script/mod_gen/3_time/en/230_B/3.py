def main():
    s = input()
    t = 'oxx' * 100000
    if s in t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()