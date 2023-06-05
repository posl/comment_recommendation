def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for i in range(1, 26):
            ss = ''
            for c in s:
                ss += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
            if ss == t:
                print('Yes')
                return
        print('No')

if __name__ == '__main__':
    main()