def main():
    s = input()
    for i in range(len(s)):
        if i%2 == 0:
            if s[i] in ['L']:
                print('No')
                return
        else:
            if s[i] in ['R']:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()