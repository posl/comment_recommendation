def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    for i in range(1, 10):
        if s[i] == '0':
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()