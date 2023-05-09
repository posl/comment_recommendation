def main():
    s = input()
    if len(set(s)) == 2 and len(list(filter(lambda x: x == 2, [s.count(c) for c in set(s)]))) == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()