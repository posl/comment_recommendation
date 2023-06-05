def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            break
    else:
        print('Yes')
        return
    for k in range(1, 26):
        u = ''
        for j in range(len(s)):
            u += chr((ord(s[j]) - ord('a') + k) % 26 + ord('a'))
        if u == t:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()