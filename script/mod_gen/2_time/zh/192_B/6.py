def main():
    S = input()
    i = 0
    for c in S:
        if i % 2 == 0:
            if c.isupper():
                print('No')
                return
        else:
            if c.islower():
                print('No')
                return
        i += 1
    print('Yes')

if __name__ == '__main__':
    main()