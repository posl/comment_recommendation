def main():
    s = input()
    if len(set(list(s))) == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()