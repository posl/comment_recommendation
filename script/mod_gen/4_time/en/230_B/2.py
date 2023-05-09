def main():
    s = input()
    t = 'o' * 100000
    if s in t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()