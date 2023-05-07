def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    for i in range(1, len(s)):
        if s[i] == '1':
            for j in range(i):
                if s[j] == '1' and s[i+1:j] == '0'*(j-i-1):
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()