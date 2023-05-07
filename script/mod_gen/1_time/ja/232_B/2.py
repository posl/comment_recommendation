def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        elif s[i] == 'a' and t[i] == 'z':
            continue
        elif s[i] == 'z' and t[i] == 'a':
            continue
        elif ord(s[i]) + 1 == ord(t[i]):
            continue
        elif ord(s[i]) - 1 == ord(t[i]):
            continue
        else:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()